from PySide6 import QtCore, QtGui, QtWidgets

class superSlider(QtWidgets.QSlider):
    """
    SUPERSLIDER creates a more flexible slider, that allows for multiple slides. In our case, it is a slider with two
    slides. One for the minimum and another for the maximum.
    """
    sliderMoved = QtCore.Signal(int, int)

    def __init__(self, *args):
        super(superSlider, self).__init__(*args)

        self.l = self.minimum()
        self.u = self.maximum()

        self.pressed_control = QtWidgets.QStyle.SC_None
        self.tick_interval = 0
        self.tick_position = QtWidgets.QSlider.NoTicks
        self.hover_control = QtWidgets.QStyle.SC_None
        self.click_offset = 0

        # 0 for the low, 1 for the high, -1 for both
        self.active_slider = 0

    def pick(self, pt):
        if self.orientation() == QtCore.Qt.Horizontal:
            return pt.x()
        else:
            return pt.y()

    def pixelPosToRangeValue(self, pos):
        opt = QtWidgets.QStyleOptionSlider()
        self.initStyleOption(opt)
        style = QtWidgets.QApplication.style()

        groove = style.subControlRect(style.CC_Slider, opt, style.SC_SliderGroove, self)
        screenHandle = style.subControlRect(style.CC_Slider, opt, style.SC_SliderHandle, self)

        if self.orientation() == QtCore.Qt.Horizontal:
            slider_length = screenHandle.width()
            slider_min = groove.x()
            slider_max = groove.right() - slider_length + 1
        else:
            slider_length = screenHandle.height()
            slider_min = groove.y()
            slider_max = groove.bottom() - slider_length + 1

        return style.sliderValueFromPosition(self.minimum(), self.maximum(), pos - slider_min, slider_max - slider_min,
                                             opt.upsideDown)

    def low(self):
        return self.l

    def setLower(self, lower):
        self.l = lower
        self.update()

    def upper(self):
        return self.u

    def setUpper(self, upper):
        self.u = upper
        self.update()

    def mousePressed(self, event):
        event.accept()

        style = QtWidgets.QApplication.style()
        btn = event.button()

        if btn:
            opt = QtWidgets.QStyleOptionSlider()
            self.initStyleOption(opt)

            self.active = -1

            for i, value in enumerate([self.l, self.u]):
                opt.sliderPosition = value
                hit = style.hitTestComplexControl(style.CC_Slider, opt, event.pos(), self)
                if hit == style.SC_SliderHandle:
                    self.active = i
                    self.pressed = hit

                    self.triggerAction(self.SliderMove)
                    self.setRepeatAction(self.SliderNoAction)
                    self.setSliderDown(True)
                    break

            if self.active < 0:
                self.pressed = QtWidgets.QStyle.SC_SliderHandle
                self.click_offset = self.pixelPosToRangeValue(self.pick(event.pos()))
                self.triggerAction(self.SliderMove)
                self.setRepeatAction(self.SliderNoAction)
        else:
            event.ignore()

    def mouseMoved(self, event):
        if self.pressed != QtWidgets.QStyle.SC_SliderHandle:
            event.ignore()
            return

        event.accept()
        new_pos = self.pixelPosToRangeValue(self.pick(event.pos()))
        opt = QtWidgets.QStyleOptionSlider()
        self.initStyleOption(opt)

        if self.active < 0:
            offset = new_pos - self.click_offset
            self.u += offset
            self.l += offset
            if self.l < self.minimum():
                diff = self.minimum() - self.l
                self.l += diff
                self.u += diff
            if self.u > self.maximum():
                diff = self.maximum() - self.u
                self.l += diff
                self.u += diff
        elif self.active_slider == 0:
            if new_pos >= self.u:
                new_pos = self.u - 1
            self.l = new_pos
        else:
            if new_pos <= self.l:
                new_pos = self.l + 1
            self.u = new_pos

        self.click_offset = new_pos

        self.update()

        self.sliderMoved.emit(self.l, self.u)
