# 随机点人应用程序 - v2.0

这是一个使用 PyQt5 开发的跨平台随机点选学生应用程序。

## 更新对比表

| 特性         | Tkinter (1.x)                           | PyQt5 (2.0)                           |
|--------------|--------------------------------------------|------------------------------------------|
| 事件循环     | 基于回调的事件循环                          | 基于信号和槽的事件驱动模型                |
| 多线程支持   | 没有内置的多线程支持                        | 内置多线程支持                           |
| 控件性能     | 基本控件，可能不是特别高效                  | 高效控件，专门为 PyQt5 设计              |
| 布局管理     | 基本布局管理，可能不是特别高效              | 高级布局管理，如 QVBoxLayout            |
| 资源管理     | 有限的资源管理，如文件读取                  | 内存映射文件读取，减少 I/O 操作          |
| 事件处理     | 基于回调的事件处理                          | 基于信号和槽的事件处理                   |
| 跨平台支持   | 有限的支持，主要针对 Windows、macOS 和 Linux | 全面的跨平台支持，包括移动设备          |
| 性能优化     | 有限的优化，如事件处理效率                  | 全面的优化，包括多线程、资源管理和布局管理 |

## 版本历史

- 1.x: [点此了解](https://github.com/RedstoneLu/LC_RSP/)

## 安装要求

- Python 3.x
- Tkinter 库（Python 标准库，无需额外安装）
- PyQt5 库（可通过 pip 安装：`pip install pyqt5`）
- 一个包含学生名单的 `students.txt` 文件，位于与 `new.py` 相同的目录下

## 运行说明

1. 确保你已经安装了 PyQt5 库。如果没有安装，可以使用以下命令进行安装：
   ```
   pip install pyqt5
   ```
2. 将学生名单文件 `students.txt` 放在与 `new.py` 相同的目录下。
3. 打开命令行或终端。
4. 导航到包含 `new.py` 和 `students.txt` 的目录。
5. 运行 `python new.py`。

## 注意事项

- 此应用程序支持 Windows、macOS 和 Linux 操作系统。
- 学生名单文件 `students.txt` 应包含学生姓名，每行一个。
   
