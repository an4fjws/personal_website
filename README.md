# 个人介绍网站

一个现代化的响应式个人介绍网站，包含首页、关于我、技能、项目展示和联系方式等模块。

## 🌐 在线访问

**[https://an4fjws.github.io/personal_website/](https://an4fjws.github.io/personal_website/)**

---

## 🖥️ 本地开发

### 方法一：直接打开
用浏览器打开 `index.html` 文件即可预览。

### 方法二：使用本地服务器（推荐）

**使用 Python：**
```bash
# Python 3
python3 -m http.server 8080

# Python 2
python -m SimpleHTTPServer 8080
```

**使用 Node.js：**
```bash
npx serve
```

**使用 PHP：**
```bash
php -S localhost:8080
```

然后在浏览器访问：`http://localhost:8080`

---

## 🚀 部署到 GitHub Pages（详细步骤）

### 第一步：创建 GitHub 仓库

1. 登录 GitHub：https://github.com
2. 点击右上角 **+** 按钮，选择 **New repository**
3. 或直接访问：https://github.com/new

4. 填写仓库信息：
   - **Repository name**: `personal_website`
   - **Description**（可选）: 个人介绍网站
   - **Public**: 选择公开（GitHub Pages 免费部署需要公开仓库）
   - **Initialize this repository with a README**: ❌ 不要勾选

5. 点击 **Create repository** 按钮

---

### 第二步：推送代码到 GitHub

#### 方式 A：使用 HTTPS + Personal Access Token（推荐）

**1. 创建 Personal Access Token**

- 访问：https://github.com/settings/tokens
- 点击 **Generate new token** → **Generate new token (classic)**
- 填写信息：
  - **Note**: `Git Push`（或其他你容易识别的名称）
  - **Expiration**: 选择 `No expiration` 或 `90 days`
  - **Select scopes**: 勾选 **repo**（全选）
- 点击 **Generate token**
- **复制 token**（以 `ghp_` 开头，⚠️ 只显示一次，请妥善保存）

**2. 推送代码**

在终端执行以下命令：

```bash
# 进入项目目录
cd /path/to/personal_website

# 初始化 Git（如果还没有初始化）
git init

# 添加所有文件
git add .

# 提交
git commit -m "Initial commit"

# 重命名分支为 main
git branch -M main

# 添加远程仓库（替换 YOUR_TOKEN 为你的 token）
git remote add origin https://an4fjws:YOUR_TOKEN@github.com/an4fjws/personal_website.git

# 推送代码
git push -u origin main
```

推送时如果需要输入：
- **Username**: `an4fjws`
- **Password**: 粘贴你的 Personal Access Token（不是 GitHub 密码）

---

#### 方式 B：使用 SSH（如果你已配置 SSH 密钥）

**1. 检查 SSH 密钥**
```bash
ls -la ~/.ssh
```

**2. 添加 SSH 公钥到 GitHub**
- 查看公钥：`cat ~/.ssh/id_rsa.pub`
- 复制公钥内容
- 访问：https://github.com/settings/keys
- 点击 **New SSH key**
- 粘贴公钥，点击 **Add SSH key**

**3. 推送代码**
```bash
cd /path/to/personal_website
git init
git add .
git commit -m "Initial commit"
git branch -M main
git remote add origin git@github.com:an4fjws/personal_website.git
git push -u origin main
```

---

### 第三步：启用 GitHub Pages

1. 进入你的仓库页面：https://github.com/an4fjws/personal_website

2. 点击顶部的 **Settings** 标签

3. 在左侧菜单栏找到并点击 **Pages**

4. 在 **Build and deployment** 区域配置：
   - **Source**: 选择 `Deploy from a branch`
   - **Branch**: 选择 `main`，文件夹选择 `/ (root)`
   - 点击 **Save** 按钮

5. 等待部署（约 1-2 分钟）
   - 页面顶部会显示进度
   - 部署完成后会显示绿色对勾和访问链接

---

### 第四步：访问你的网站

部署完成后，访问：

**https://an4fjws.github.io/personal_website/**

---

## ✏️ 自定义内容

编辑 `index.html` 文件，修改以下信息：

### 基本信息
- 姓名：搜索 `张三` 替换为你的名字
- 邮箱：搜索 `zhangsan@email.com` 替换为你的邮箱
- 电话：搜索 `+86 138 0000 0000` 替换为你的电话
- 地址：搜索 `北京市朝阳区` 替换为你的所在地

### 技能列表
在 `<section id="skills">` 中修改技能卡片内容

### 项目展示
在 `<section id="projects">` 中修改项目信息：
- 项目名称
- 项目描述
- 技术标签
- 项目链接

### 社交链接
在 `<section id="contact">` 中修改社交链接：
- GitHub
- LinkedIn
- 知乎等

---

## 📁 文件结构

```
personal_website/
├── index.html      # 主页面（HTML 结构）
├── styles.css      # 样式文件（CSS 样式）
├── script.js       # 交互脚本（JavaScript 功能）
├── README.md       # 说明文档
└── .gitignore      # Git 忽略文件
```

---

## 🎨 技术栈

- **HTML5** - 语义化结构
- **CSS3** - 响应式设计、渐变、动画
- **JavaScript** - 原生 JS，无依赖
- **Google Fonts** - Noto Sans SC 中文字体

---

## 📱 响应式支持

网站已适配以下设备：
- 🖥️ 桌面端（1200px+）
- 💻 笔记本（768px - 1199px）
- 📱 平板（481px - 767px）
- 📱 手机（≤480px）

---

## 📝 更新网站

修改内容后，推送更新：

```bash
git add .
git commit -m "更新个人信息"
git push
```

GitHub Pages 会自动重新部署，约 1 分钟后生效。

---

## 📄 License

MIT License - 可自由使用和修改

---

## 🙋 问题反馈

如有问题，请提 Issue 或联系作者。
