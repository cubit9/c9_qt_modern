# C9 Qt Modern

**C9 Qt Modern** is a Python package aimed to make PySide applications
look better and consistent on multiple platforms. It provides a custom
frameless window and a dark theme. The initial idea comes from this
project [Qt Frameless Window
DarkStyle](https://github.com/Jorgen-VikingGod/Qt-Frameless-Window-DarkStyle).

![Example](examples/mainwindow.png){.align-center width="450px"}

## Installation

The recommended way to install is by using `pip`, i.e:

``` {.sh caption="Installation"}
pip install c9_qt_modern
```

## Usage

In order to use [c9_qt_modern]{.title-ref}, simply apply the style you
want to your application and then, create a [ModernWindow]{.title-ref}
enclosing the window you want to *modernize*:

``` {.python caption="Usage"}
import c9_qt_modern.styles
import c9_qt_modern.windows

...

app = QApplication()
win = YourWindow()

c9_qt_modern.styles.dark(app)

mw = c9_qt_modern.windows.ModernWindow(win)
mw.show()

...
```
