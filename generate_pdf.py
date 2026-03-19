#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from reportlab.lib import colors
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import inch, cm
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, PageBreak, Table, TableStyle, ListFlowable, ListItem
from reportlab.lib.enums import TA_CENTER, TA_LEFT, TA_JUSTIFY
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.lib.colors import HexColor
import os

def create_pdf():
    """创建个人网站构建与部署指南 PDF 文档"""
    
    # 创建 PDF 文档
    doc = SimpleDocTemplate(
        "个人网站构建与部署指南.pdf",
        pagesize=A4,
        rightMargin=2*cm,
        leftMargin=2*cm,
        topMargin=2*cm,
        bottomMargin=2*cm
    )
    
    # 存储内容的列表
    story = []
    
    # 注册中文字体（使用系统字体）
    font_paths = [
        "/System/Library/Fonts/PingFang.ttc",
        "/System/Library/Fonts/PingFang SC.ttc",
        "/Library/Fonts/PingFang.ttc",
        "/System/Library/Fonts/STHeiti Light.ttc",
        "/System/Library/Fonts/Supplemental/PingFang.ttc",
    ]
    
    chinese_font = None
    for font_path in font_paths:
        if os.path.exists(font_path):
            try:
                pdfmetrics.registerFont(TTFont('ChineseFont', font_path))
                chinese_font = 'ChineseFont'
                break
            except:
                continue
    
    # 定义样式
    styles = getSampleStyleSheet()
    
    # 标题样式
    title_style = ParagraphStyle(
        'CustomTitle',
        parent=styles['Heading1'],
        fontName=chinese_font if chinese_font else 'Helvetica-Bold',
        fontSize=24,
        textColor=HexColor('#667eea'),
        spaceAfter=30,
        alignment=TA_CENTER,
        leading=32
    )
    
    subtitle_style = ParagraphStyle(
        'CustomSubtitle',
        parent=styles['Normal'],
        fontName=chinese_font if chinese_font else 'Helvetica',
        fontSize=14,
        textColor=colors.gray,
        spaceAfter=20,
        alignment=TA_CENTER,
        leading=20
    )
    
    h1_style = ParagraphStyle(
        'CustomH1',
        parent=styles['Heading1'],
        fontName=chinese_font if chinese_font else 'Helvetica-Bold',
        fontSize=18,
        textColor=HexColor('#667eea'),
        spaceAfter=15,
        spaceBefore=20,
        leading=24
    )
    
    h2_style = ParagraphStyle(
        'CustomH2',
        parent=styles['Heading2'],
        fontName=chinese_font if chinese_font else 'Helvetica-Bold',
        fontSize=14,
        textColor=HexColor('#2d3748'),
        spaceAfter=10,
        spaceBefore=15,
        leading=18
    )
    
    normal_style = ParagraphStyle(
        'CustomNormal',
        parent=styles['Normal'],
        fontName=chinese_font if chinese_font else 'Helvetica',
        fontSize=11,
        textColor=HexColor('#2d3748'),
        spaceAfter=8,
        leading=16,
        alignment=TA_JUSTIFY
    )
    
    code_style = ParagraphStyle(
        'CustomCode',
        parent=styles['Normal'],
        fontName='Courier',
        fontSize=9,
        textColor=HexColor('#2d3748'),
        spaceAfter=10,
        spaceBefore=5,
        leading=12,
        backColor=HexColor('#f7fafc'),
        leftIndent=10
    )
    
    bullet_style = ParagraphStyle(
        'CustomBullet',
        parent=styles['Normal'],
        fontName=chinese_font if chinese_font else 'Helvetica',
        fontSize=11,
        textColor=HexColor('#2d3748'),
        spaceAfter=5,
        leading=16,
        leftIndent=20
    )
    
    # ========== 封面 ==========
    story.append(Spacer(1, 2*inch))
    
    # 标题
    story.append(Paragraph("个人网站构建与部署指南", title_style))
    story.append(Spacer(1, 20))
    
    # 副标题
    story.append(Paragraph("从零开始搭建并部署你的个人介绍网站", subtitle_style))
    story.append(Spacer(1, 1*inch))
    
    # 作者信息
    info_style = ParagraphStyle(
        'InfoStyle',
        parent=styles['Normal'],
        fontName=chinese_font if chinese_font else 'Helvetica',
        fontSize=11,
        textColor=colors.darkgrey,
        alignment=TA_CENTER,
        leading=18
    )
    
    story.append(Paragraph("作者：AN4FJWS", info_style))
    story.append(Paragraph("GitHub: https://github.com/an4fjws/personal_website", info_style))
    story.append(Paragraph("在线访问：https://an4fjws.github.io/personal_website/", info_style))
    story.append(Paragraph("生成日期：2026 年 3 月", info_style))
    
    story.append(PageBreak())
    
    # ========== 第一章 ==========
    story.append(Paragraph("第一章：项目概述", h1_style))
    
    story.append(Paragraph("1.1 项目简介", h2_style))
    story.append(Paragraph(
        "本项目是一个现代化的响应式个人介绍网站，包含首页、关于我、技能展示、"
        "项目展示和联系方式等模块。网站采用纯 HTML/CSS/JavaScript 构建，无需任何框架依赖，"
        "可以免费部署在 GitHub Pages 上。",
        normal_style
    ))
    
    story.append(Paragraph("1.2 技术栈", h2_style))
    tech_stack = [
        ("HTML5", "语义化页面结构"),
        ("CSS3", "响应式设计、渐变背景、动画效果"),
        ("JavaScript", "原生 JS，无第三方依赖"),
        ("GitHub Pages", "免费静态网站托管"),
    ]
    
    for tech, desc in tech_stack:
        story.append(Paragraph(f"• <b>{tech}</b> - {desc}", bullet_style))
    
    story.append(Paragraph("1.3 功能特性", h2_style))
    features = [
        ("响应式设计", "适配桌面、平板、手机等各种设备"),
        ("平滑滚动", "导航栏点击平滑滚动到对应区域"),
        ("移动端菜单", "汉堡菜单适配小屏幕"),
        ("滚动动画", "元素进入视口时触发动画"),
        ("回到顶部", "滚动后显示回到顶部按钮"),
        ("联系表单", "内置联系表单（需后端支持）"),
    ]
    
    for feature, desc in features:
        story.append(Paragraph(f"• <b>{feature}</b> - {desc}", bullet_style))
    
    story.append(PageBreak())
    
    # ========== 第二章 ==========
    story.append(Paragraph("第二章：本地开发环境", h1_style))
    
    story.append(Paragraph("2.1 前置要求", h2_style))
    story.append(Paragraph("请确保你的计算机已安装以下工具：", normal_style))
    
    requirements = [
        ("Git", "版本控制工具，https://git-scm.com/"),
        ("文本编辑器", "VS Code、Sublime Text 或任意编辑器"),
        ("现代浏览器", "Chrome、Firefox、Safari 等"),
    ]
    
    for tool, desc in requirements:
        story.append(Paragraph(f"• <b>{tool}</b> - {desc}", bullet_style))
    
    story.append(Paragraph("2.2 获取项目代码", h2_style))
    story.append(Paragraph("方法一：从 GitHub 克隆（如果已有仓库）", normal_style))
    story.append(Paragraph("git clone https://github.com/an4fjws/personal_website.git", code_style))
    story.append(Paragraph("cd personal_website", code_style))
    
    story.append(Paragraph("方法二：直接下载 ZIP 文件", normal_style))
    story.append(Paragraph("访问 https://github.com/an4fjws/personal_website，点击 \"Code\" → \"Download ZIP\"，解压即可。", normal_style))
    
    story.append(Paragraph("2.3 本地预览", h2_style))
    story.append(Paragraph("方法一：直接打开", normal_style))
    story.append(Paragraph("双击 index.html 文件，用浏览器打开即可预览。", normal_style))
    
    story.append(Paragraph("方法二：使用本地服务器（推荐）", normal_style))
    story.append(Paragraph("<b>Python 3:</b>", normal_style))
    story.append(Paragraph("python3 -m http.server 8080", code_style))
    
    story.append(Paragraph("<b>Node.js:</b>", normal_style))
    story.append(Paragraph("npx serve", code_style))
    
    story.append(Paragraph("然后在浏览器访问：http://localhost:8080", normal_style))
    
    story.append(PageBreak())
    
    # ========== 第三章 ==========
    story.append(Paragraph("第三章：自定义内容", h1_style))
    
    story.append(Paragraph("3.1 修改个人信息", h2_style))
    story.append(Paragraph("打开 index.html 文件，搜索并替换以下内容：", normal_style))
    
    # 创建表格
    table_data = [
        ["搜索内容", "替换为"],
        ["张三", "你的姓名"],
        ["zhangsan@email.com", "你的邮箱"],
        ["+86 138 0000 0000", "你的电话"],
        ["北京市朝阳区", "你的所在地"],
        ["全栈开发工程师", "你的职业/头衔"],
    ]
    
    table = Table(table_data, colWidths=[3*cm, 5*cm])
    table.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), HexColor('#667eea')),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
        ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
        ('FONTNAME', (0, 0), (-1, 0), chinese_font if chinese_font else 'Helvetica-Bold'),
        ('FONTSIZE', (0, 0), (-1, 0), 11),
        ('BOTTOMPADDING', (0, 0), (-1, 0), 10),
        ('BACKGROUND', (0, 1), (-1, -1), colors.beige),
        ('TEXTCOLOR', (0, 1), (-1, -1), colors.black),
        ('FONTNAME', (0, 1), (-1, -1), chinese_font if chinese_font else 'Helvetica'),
        ('FONTSIZE', (0, 1), (-1, -1), 10),
        ('GRID', (0, 0), (-1, -1), 0.5, colors.grey),
    ]))
    
    story.append(table)
    story.append(Spacer(1, 20))
    
    story.append(Paragraph("3.2 修改技能列表", h2_style))
    story.append(Paragraph("在 index.html 中找到 &lt;section id=\"skills\"&gt;，修改技能卡片内容：", normal_style))
    story.append(Paragraph("每个技能卡片包含：技能图标、技能分类标题、技能列表项。", normal_style))
    
    story.append(Paragraph("3.3 修改项目展示", h2_style))
    story.append(Paragraph("在 index.html 中找到 &lt;section id=\"projects\"&gt;，修改：", normal_style))
    story.append(Paragraph("项目名称、项目描述、技术标签、项目链接（GitHub/在线演示）。", normal_style))
    
    story.append(Paragraph("3.4 修改社交链接", h2_style))
    story.append(Paragraph("在 index.html 中找到 &lt;section id=\"contact\"&gt;，修改社交链接：", normal_style))
    
    social = [
        ("GitHub", "https://github.com/你的用户名"),
        ("LinkedIn", "https://linkedin.com/in/你的用户名"),
        ("知乎", "https://zhihu.com/people/你的用户名"),
    ]
    
    for platform, url in social:
        story.append(Paragraph(f"• {platform}: {url}", bullet_style))
    
    story.append(PageBreak())
    
    # ========== 第四章 ==========
    story.append(Paragraph("第四章：部署到 GitHub Pages", h1_style))
    
    story.append(Paragraph("4.1 创建 GitHub 账号", h2_style))
    story.append(Paragraph("如果没有 GitHub 账号，请访问 https://github.com 注册。", normal_style))
    
    story.append(Paragraph("4.2 创建 GitHub 仓库", h2_style))
    
    steps = [
        "登录 GitHub：https://github.com",
        "点击右上角 + 按钮，选择 New repository，或直接访问 https://github.com/new",
        "填写仓库信息：",
    ]
    
    for i, step in enumerate(steps, 1):
        story.append(Paragraph(f"{i}. {step}", normal_style))
    
    sub_items = [
        "Repository name: personal_website",
        "Description（可选）: 个人介绍网站",
        "Public: 选择公开（免费部署需要公开仓库）",
        "Initialize this repository with a README: 不要勾选",
    ]
    
    for item in sub_items:
        story.append(Paragraph(f"   • {item}", bullet_style))
    
    story.append(Paragraph("点击 Create repository 按钮创建仓库。", normal_style))
    
    story.append(Paragraph("4.3 配置 Git 环境", h2_style))
    story.append(Paragraph("打开终端（Terminal），执行以下命令：", normal_style))
    
    config_steps = [
        ("1. 配置 Git 用户名和邮箱：", 'git config --global user.name "你的用户名"\ngit config --global user.email "你的邮箱@example.com"'),
        ("2. 初始化本地 Git 仓库：", 'cd /path/to/personal_website\ngit init'),
        ("3. 添加并提交文件：", 'git add .\ngit commit -m "Initial commit"'),
        ("4. 重命名分支为 main：", 'git branch -M main'),
    ]
    
    for desc, code in config_steps:
        story.append(Paragraph(desc, normal_style))
        story.append(Paragraph(code, code_style))
    
    story.append(PageBreak())
    
    story.append(Paragraph("4.4 创建 Personal Access Token", h2_style))
    story.append(Paragraph("GitHub 已不再支持使用密码进行 Git 操作，需要使用 Personal Access Token：", normal_style))
    
    token_steps = [
        "访问 https://github.com/settings/tokens",
        "点击 Generate new token → Generate new token (classic)",
        "填写信息：",
    ]
    
    for i, step in enumerate(token_steps, 1):
        story.append(Paragraph(f"{i}. {step}", normal_style))
    
    token_info = [
        "Note: Git Push（或其他易识别的名称）",
        "Expiration: No expiration 或 90 days",
        "Select scopes: 勾选 repo（全选）",
    ]
    
    for info in token_info:
        story.append(Paragraph(f"   • {info}", bullet_style))
    
    story.append(Paragraph("点击 Generate token，复制生成的 token（以 ghp_ 开头，只显示一次，请妥善保存！）", normal_style))
    
    story.append(Paragraph("4.5 推送代码到 GitHub", h2_style))
    story.append(Paragraph("方法一：使用 Personal Access Token（推荐）", normal_style))
    story.append(Paragraph("在终端执行：", normal_style))
    
    push_code = """cd /path/to/personal_website
git remote add origin https://你的用户名:YOUR_TOKEN@github.com/你的用户名/personal_website.git
git push -u origin main"""
    story.append(Paragraph(push_code, code_style))
    
    story.append(Paragraph("将 YOUR_TOKEN 替换为你刚才复制的 token，将 你的用户名 替换为你的实际 GitHub 用户名。", normal_style))
    
    story.append(Paragraph("推送时如果需要输入：", normal_style))
    story.append(Paragraph("Username: 你的 GitHub 用户名", code_style))
    story.append(Paragraph("Password: 粘贴你的 Personal Access Token", code_style))
    
    story.append(Paragraph("方法二：使用 SSH（如果已配置 SSH 密钥）", normal_style))
    story.append(Paragraph("git remote add origin git@github.com:你的用户名/personal_website.git", code_style))
    story.append(Paragraph("git push -u origin main", code_style))
    
    story.append(PageBreak())
    
    story.append(Paragraph("4.6 启用 GitHub Pages", h2_style))
    
    pages_steps = [
        "进入你的仓库页面：https://github.com/你的用户名/personal_website",
        "点击顶部的 Settings 标签",
        "在左侧菜单栏找到并点击 Pages",
        "在 Build and deployment 区域配置：",
    ]
    
    for i, step in enumerate(pages_steps, 1):
        story.append(Paragraph(f"{i}. {step}", normal_style))
    
    pages_info = [
        "Source: 选择 Deploy from a branch",
        "Branch: 选择 main，文件夹选择 / (root)",
    ]
    
    for info in pages_info:
        story.append(Paragraph(f"   • {info}", bullet_style))
    
    story.append(Paragraph("点击 Save 按钮保存设置。", normal_style))
    
    story.append(Paragraph("4.7 访问你的网站", h2_style))
    story.append(Paragraph("等待 1-2 分钟部署完成后，访问：", normal_style))
    
    url_para = Paragraph(
        "<b>https://你的用户名.github.io/personal_website/</b>",
        ParagraphStyle(
            'URLStyle',
            parent=styles['Normal'],
            fontName=chinese_font if chinese_font else 'Helvetica-Bold',
            fontSize=12,
            textColor=HexColor('#0066cc'),
            alignment=TA_CENTER,
            leading=18
        )
    )
    story.append(url_para)
    story.append(Spacer(1, 20))
    story.append(Paragraph("部署状态可以在仓库的 Actions 标签页查看。", normal_style))
    
    story.append(PageBreak())
    
    # ========== 第五章 ==========
    story.append(Paragraph("第五章：后续维护", h1_style))
    
    story.append(Paragraph("5.1 更新网站内容", h2_style))
    story.append(Paragraph("修改文件后，推送更新：", normal_style))
    story.append(Paragraph("git add .\ngit commit -m \"更新说明\"\ngit push", code_style))
    story.append(Paragraph("GitHub Pages 会自动重新部署，约 1 分钟后生效。", normal_style))
    
    story.append(Paragraph("5.2 绑定自定义域名（可选）", h2_style))
    story.append(Paragraph("如果你想使用自己的域名（如 www.yourname.com）：", normal_style))
    
    domain_steps = [
        "在域名注册商处添加 CNAME 记录，指向 你的用户名.github.io",
        "在仓库根目录创建 CNAME 文件，内容为你的域名（如：www.yourname.com）",
        "在仓库 Settings → Pages → Custom domain 中填写你的域名",
        "点击 Save 保存",
    ]
    
    for i, step in enumerate(domain_steps, 1):
        story.append(Paragraph(f"{i}. {step}", normal_style))
    
    story.append(Paragraph("5.3 查看部署日志", h2_style))
    story.append(Paragraph("访问 https://github.com/你的用户名/personal_website/actions 查看部署历史和日志。", normal_style))
    
    story.append(Paragraph("5.4 安全提示", h2_style))
    story.append(Paragraph("⚠️ 重要：Personal Access Token 只在首次推送时使用，建议：", normal_style))
    
    security_tips = [
        "不要将 Token 提交到代码仓库",
        "Token 泄露后立即删除并重新生成",
        "可以使用 Git 凭据管理器保存 Token",
        "考虑使用 SSH 密钥代替 Token",
    ]
    
    for tip in security_tips:
        story.append(Paragraph(f"• {tip}", bullet_style))
    
    story.append(PageBreak())
    
    # ========== 第六章 ==========
    story.append(Paragraph("第六章：常见问题", h1_style))
    
    faq = [
        ("Q: 推送时提示 \"Repository not found\"", 
         "A: 确保已在 GitHub 创建仓库，且仓库名称正确。检查远程仓库地址：git remote -v"),
        
        ("Q: 推送时认证失败", 
         "A: 确保使用 Personal Access Token 而非密码。Token 需要 repo 权限。"),
        
        ("Q: GitHub Pages 显示 404", 
         "A: 等待 1-2 分钟部署完成。检查 Settings → Pages 配置是否正确。确保仓库是公开的。"),
        
        ("Q: 修改后网站没有更新", 
         "A: 清除浏览器缓存（Ctrl+Shift+Delete 或 Cmd+Shift+Delete）。检查是否已成功推送：git log"),
        
        ("Q: 如何删除已部署的网站", 
         "A: 在 Settings → Pages 中将 Source 改为 None，或删除 GitHub 仓库。"),
    ]
    
    for question, answer in faq:
        story.append(Paragraph(question, ParagraphStyle(
            'FAQQuestion',
            parent=styles['Normal'],
            fontName=chinese_font if chinese_font else 'Helvetica-Bold',
            fontSize=11,
            textColor=HexColor('#2d3748'),
            spaceAfter=5,
            leading=16
        )))
        story.append(Paragraph(answer, normal_style))
        story.append(Spacer(1, 15))
    
    story.append(PageBreak())
    
    # ========== 附录 ==========
    story.append(Paragraph("附录", h1_style))
    
    story.append(Paragraph("A. 项目文件结构", h2_style))
    story.append(Paragraph("""personal_website/
├── index.html      # 主页面（HTML 结构）
├── styles.css      # 样式文件（CSS 样式）
├── script.js       # 交互脚本（JavaScript 功能）
├── README.md       # 项目说明文档
├── .gitignore      # Git 忽略文件
└── generate_doc.py # 文档生成脚本""", code_style))
    
    story.append(Paragraph("B. 有用链接", h2_style))
    links = [
        ("项目仓库", "https://github.com/an4fjws/personal_website"),
        ("在线演示", "https://an4fjws.github.io/personal_website/"),
        ("GitHub Pages 文档", "https://pages.github.com/"),
        ("Git 下载", "https://git-scm.com/"),
        ("VS Code", "https://code.visualstudio.com/"),
    ]
    
    for name, url in links:
        story.append(Paragraph(f"• <b>{name}</b>: {url}", bullet_style))
    
    story.append(Paragraph("C. 技术支持", h2_style))
    story.append(Paragraph("如有问题，请：", normal_style))
    
    support_steps = [
        "查看本指南是否已解答你的问题",
        "在 GitHub 仓库提 Issue",
        "查阅官方文档：https://docs.github.com/en/pages",
    ]
    
    for i, step in enumerate(support_steps, 1):
        story.append(Paragraph(f"{i}. {step}", normal_style))
    
    # ========== 页脚 ==========
    story.append(PageBreak())
    footer_style = ParagraphStyle(
        'FooterStyle',
        parent=styles['Normal'],
        fontName=chinese_font if chinese_font else 'Helvetica',
        fontSize=10,
        textColor=colors.darkgrey,
        alignment=TA_CENTER,
        leading=14
    )
    
    story.append(Spacer(1, 1*inch))
    story.append(Paragraph("───", footer_style))
    story.append(Paragraph("文档生成完成。祝你部署顺利！", footer_style))
    story.append(Paragraph("如有问题，请访问：https://github.com/an4fjws/personal_website", footer_style))
    
    # 构建 PDF
    doc.build(story)
    print("✅ PDF 文档已生成：个人网站构建与部署指南.pdf")

if __name__ == '__main__':
    create_pdf()
