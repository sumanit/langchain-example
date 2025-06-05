# Python

Python是一切的基础 以`mac系统` `Python3.11`为例，针对不同的安装方式 安装目录有所不同

安装后自动生成指向 Python 可执行文件的软链接（如 `python3` → `/Library/Frameworks/.../python3`），便于终端直接调用

- 安装目录

  - brew安装 
    - **主目录：**`/opt/homebrew/Cellar/python@X.X/X.X.X`
    - **命令：**`/opt/homebrew/bin/python3` -> `主目录/bin/python3`

  - 官网安装包安装 `/Library/Frameworks/Python.framework/Versions/python3`
    - **主目录：** `/Library/Frameworks/Python.framework/Versions/X.X/bin/python3`
    - **命令：**`/usr/local/bin`

  - 系统内置
    - **主目录：** `/Library/Developer/CommandLineTools/Library/Frameworks/Python3.framework`
    - **命令：**`/usr/bin/python3`

安装后系统会安装以下文件

- **主目录:**
  
  - **bin:**  存放 Python 相关的可执行文件和脚本
  - **lib: ** 存放 Python 标准库和第三方包
  - **include:** 存放 C/C++ 头文件，用于编译 Python 扩展模块或嵌入 Python 到其他程序
  - **etc:** 存放配置文件（非标准目录，某些特定场景下可能存在）
  - **share:** 存放共享数据文件（如文档、示例代码、许可证信息）
  - **Headers:** 指向 `include` 目录的软链接，为兼容某些编译工具链而存在
  - **Resources(Mac特有)**: 存放与 Python 相关的资源文件（如文档、图标、配置文件）
  - **Python: **Python解释器可执行文件
  - **CodeSignature:** _CodeSignature
  
- **命令:**

  - python3 
  - python
  - pip
  - pip3
  - pydoc3
  - pydoc3.11
  - python3-config
  - python3.11-config
  - python3-intel64
  - python3.11-intel64
  
  -------
  
  
  

# 依赖管理

| **功能维度**   | **Poetry**                                                   | **pip**                                          | **核心差异总结**                                             |
| -------------- | ------------------------------------------------------------ | ------------------------------------------------ | ------------------------------------------------------------ |
| **依赖管理**   | 自动解析依赖树并生成 `poetry.lock`，避免版本冲突             | 仅安装直接声明的依赖，需手动解决冲突             | Poetry 提供完整的依赖链管理，pip 依赖人工干预                |
| **虚拟环境**   | 内置虚拟环境管理，自动创建和激活                             | 需配合 `venv`/`virtualenv` 手动管理              | Poetry 集成化更高，减少环境配置步骤                          |
| **版本控制**   | 通过 `pyproject.toml` 声明版本范围，`poetry.lock` 锁定精确版本 | 依赖 `requirements.txt` 手动记录版本，无自动锁定 | Poetry 确保跨环境一致性，pip 需额外工具（如 `pip-tools`）实现类似功能 |
| **项目结构**   | 标准化模板初始化项目（`poetry init`），支持元数据管理        | 依赖开发者自定义结构，无内置模板                 | Poetry 提升协作效率，pip 灵活性高但规范性弱                  |
| **包发布**     | 内置打包和发布功能（`poetry publish`）                       | 需结合 `setuptools` 和 `twine` 手动发布          | Poetry 简化发布流程，适合高频维护的开源项目                  |
| **跨平台支持** | 兼容主流操作系统，但对旧版 Python 支持有限                   | 全版本 Python 原生支持，稳定性强                 | pip 适用性更广，Poetry 依赖现代 Python 生态                  |
| **性能**       | 依赖解析较慢（尤其复杂项目），但锁定机制提升可靠性           | 安装速度快，但依赖冲突时调试成本高               | Poetry 牺牲部分速度换取稳定性，pip 适合轻量级场景            |
| **适用场景**   | 中大型项目、团队协作、需严格版本控制或包发布                 | 小型脚本、快速原型开发、简单依赖管理             | Poetry 适合长期维护项目，pip 适合轻量需求                    |

## Pip

pip是Python内置命令,用于安装和管理python包

全局安装包位于  `/Library/Frameworks/Python.framework/Versions/3.11/lib/python3.11/site-packages/pandas` 

用户安装包位于 `~/Library/Python/3.11/lib/python/site-packages`

> **Python 解释器优先加载 `user 级别` 安装的包，其次才是 `全局级别` 的包 **
>
> **若同一包在两个级别均有安装，默认使用 `user 级别` 的版本**

- 安装包 `pip install`
- 卸载包 `pip uninstall`
- 升级包 `pip install --upgrade`
- 查看包 `pip list` 
- 生成依赖文件 `pip freeze > requirements.txt`
- 安装依赖 `pip install -r requirements.txt`

- 查看包 `pip show`

- 搜索包 `pip search` 

- 清理缓存 `pip cache purge`

## Poetry

poetry更类似于maven 会为每个项目独立维护一套依赖 而且本身可以做虚拟环境管理

安装包位于 /Users/suman/Library/Caches/pypoetry/virtualenvs/项目-随机码-py版本/lib

Poetry 是一个现代化的 **Python 项目依赖管理和打包工具**，通过统一配置文件和自动化流程简化开发流程。以下是其核心特性和使用方法：

1. **依赖管理**
   - 自动解析并安装依赖项，支持版本锁定（通过 `poetry.lock` 文件）。
   - 区分生产依赖和开发依赖，例如 `poetry add requests`（生产）和 `poetry add pytest --dev`（开发）。
   - 解决依赖冲突，确保环境一致性。
2. **虚拟环境管理**
   - 自动创建项目专属虚拟环境，支持通过 `poetry config virtualenvs.in-project true` 设置虚拟环境存储路径。
   - 通过 `poetry shell` 激活虚拟环境，`poetry run` 直接运行脚本。
3. **项目配置与打包**
   - 使用 `pyproject.toml` 文件统一管理项目元数据、依赖和构建配置。
   - 支持构建（`poetry build`）和发布（`poetry publish`）包到 PyPI 或私有仓库。



# 虚拟环境管理

## **为什么需要虚拟环境？**

- **依赖隔离**：不同项目可能需要不同版本的 Python 包（如 Django 2.x vs 3.x），虚拟环境确保每个项目使用独立的依赖。
- **避免全局污染**：直接全局安装包可能导致版本冲突，甚至影响系统工具。
- **方便协作**：通过配置文件（如 `requirements.txt`）快速复现环境

## 各种工具对比

| 特性         | venv                  | virtualenv     | conda                                   |
| ------------ | --------------------- | -------------- | --------------------------------------- |
| **所属类型** | Python 标准库（3.3+） | 第三方工具     | 独立跨平台工具（Anaconda/Miniconda）    |
| **语言支持** | 仅 Python             | 仅 Python      | Python + 多语言（R、C++等）26           |
| **包管理**   | 依赖 pip              | 依赖 pip       | 自带包管理（支持非 Python 包）23        |
| **环境隔离** | 仅 Python 依赖        | 仅 Python 依赖 | 全系统依赖（包括 Python 和非 Python）26 |
| **跨平台性** | 是                    | 是             | 是                                      |
| **安装体积** | 无需安装              | 轻量           | 较大（Anaconda 约 5-6GB）3              |

## 工具详细介绍

### venv

Python内置虚拟环境管理工具

- 创建虚拟环境

  ```bash
  # 语法
  python -m venv <环境目录路径>
  # 示例：在当前目录创建名为 myenv 的环境
  python -m venv myenv
  ```

- 激活虚拟环境

  ```bash
  source myenv/bin/activate   # 激活
  deactivate                  # 退出
  ```

### virtualenv

- 安装 Virtualenv

  ```bash
  # 全局安装（需管理员权限）
  pip install virtualenv
  # 用户级安装（无需管理员权限）
  pip install --user virtualenv
  ```

- 创建虚拟环境

  ```bash
  # 创建名为 myenv 的虚拟环境（默认使用当前 Python 版本）
  virtualenv myenv
  # 指定 Python 解释器路径创建环境（如 -p python3.7）
  virtualenv -p /path/to/python myenv
  ```

- 激活虚拟环境

  ```bash
  source myenv/bin/activate  # 激活
  deactivate                 # 退出
  ```

你好！[**月经不调**](#{"type":"kkContentSymptom","params":{"contentId":"35557210598400"}})


### conda

（科学计算场景）：跨语言依赖管理，支持环境隔离

# 其他工具

## pipx

1. **python 应用程序管理**
   pipx 专用于安装和运行带有 CLI 入口的 Python 应用（如 `poetry`、`black`），每个应用独立安装在隔离的虚拟环境中，避免全局环境污染和版本冲突问题
2. **虚拟环境隔离**
   每次安装应用时，pipx 会自动创建独立的虚拟环境，确保依赖包互不影响（例如 `pylint` 和 `pyinstaller` 可共存不同环境中）
3. **简化操作**
   支持一键安装、升级、卸载应用，并自动管理环境变量，方便直接在终端调用