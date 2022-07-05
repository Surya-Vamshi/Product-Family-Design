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

    def mousePressEvent(self, event):
        event.accept()

        style = QtWidgets.QApplication.style()
        button = event.button()

        # In a normal slider control, when the user clicks on a point in the
        # slider's total range, but not on the slider part of the control the
        # control would jump the slider value to where the user clicked.
        # For this control, clicks which are not direct hits will slide both
        # slider parts

        if button:
            opt = QtWidgets.QStyleOptionSlider()
            self.initStyleOption(opt)

            self.active_slider = -1

            for i, value in enumerate([self.l, self.u]):
                opt.sliderPosition = value
                hit = style.hitTestComplexControl(style.CC_Slider, opt, event.pos(), self)
                if hit == style.SC_SliderHandle:
                    self.active_slider = i
                    self.pressed_control = hit

                    self.triggerAction(self.SliderMove)
                    self.setRepeatAction(self.SliderNoAction)
                    self.setSliderDown(True)
                    break

            if self.active_slider < 0:
                self.pressed_control = QtWidgets.QStyle.SC_SliderHandle
                self.click_offset = self.pixelPosToRangeValue(self.pick(event.pos()))
                self.triggerAction(self.SliderMove)
                self.setRepeatAction(self.SliderNoAction)
        else:
            event.ignore()

    def mouseMoveEvent(self, event):
        if self.pressed_control != QtWidgets.QStyle.SC_SliderHandle:
            event.ignore()
            return

        event.accept()
        new_pos = self.pixelPosToRangeValue(self.pick(event.pos()))
        opt = QtWidgets.QStyleOptionSlider()
        self.initStyleOption(opt)

        if self.active_slider < 0:
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

        # self.emit(QtCore.SIGNAL('sliderMoved(int)'), new_pos)
        self.sliderMoved.emit(self.l, self.u)

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

    def paintEvent(self, event):
        painter = QtGui.QPainter(self)
        style = QtWidgets.QApplication.style()

        opt = QtWidgets.QStyleOptionSlider()
        self.initStyleOption(opt)
        opt.siderValue = 0
        opt.sliderPosition = 0
        opt.subControls = QtWidgets.QStyle.SC_SliderGroove
        if self.tickPosition() != self.NoTicks:
            opt.subControls |= QtWidgets.QStyle.SC_SliderTickmarks
        style.drawComplexControl(QtWidgets.QStyle.CC_Slider, opt, painter, self)
        groove = style.subControlRect(QtWidgets.QStyle.CC_Slider, opt, QtWidgets.QStyle.SC_SliderGroove, self)

        self.initStyleOption(opt)
        opt.subControls = QtWidgets.QStyle.SC_SliderGroove

        opt.siderValue = 0
        opt.sliderPosition = self.l
        low_rect = style.subControlRect(QtWidgets.QStyle.CC_Slider, opt, QtWidgets.QStyle.SC_SliderHandle, self)
        opt.sliderPosition = self.u
        high_rect = style.subControlRect(QtWidgets.QStyle.CC_Slider, opt, QtWidgets.QStyle.SC_SliderHandle, self)

        low_pos = self.pick(low_rect.center())
        high_pos = self.pick(high_rect.center())

        min_pos = min(low_pos, high_pos)
        max_pos = max(low_pos, high_pos)

        c = QtCore.QRect(low_rect.center(), high_rect.center()).center()

        if opt.orientation == QtCore.Qt.Horizontal:
            span_rect = QtCore.QRect(QtCore.QPoint(min_pos, c.y() - 2), QtCore.QPoint(max_pos, c.y() + 1))
        else:
            span_rect = QtCore.QRect(QtCore.QPoint(c.x() - 2, min_pos), QtCore.QPoint(c.x() + 1, max_pos))

        if opt.orientation == QtCore.Qt.Horizontal:
            groove.adjust(0, 0, -1, 0)
        else:
            groove.adjust(0, 0, 0, -1)

        highlight = self.palette().color(QtGui.QPalette.Highlight)
        painter.setBrush(QtGui.QBrush(highlight))
        painter.setPen(QtGui.QPen(highlight, 0))
        painter.drawRect(span_rect.intersected(groove))

        for i, value in enumerate([self.l, self.u]):
            opt = QtWidgets.QStyleOptionSlider()
            self.initStyleOption(opt)

            if i == 0:
                opt.subControls = QtWidgets.QStyle.SC_SliderHandle
            else:
                opt.subControls = QtWidgets.QStyle.SC_SliderHandle

            if self.tickPosition() != self.NoTicks:
                opt.subControls |= QtWidgets.QStyle.SC_SliderTickmarks

            if self.pressed_control:
                opt.activeSubControls = self.pressed_control
            else:
                opt.activeSubControls = self.hover_control

            opt.sliderPosition = value
            opt.sliderValue = value
            style.drawComplexControl(QtWidgets.QStyle.CC_Slider, opt, painter, self)
