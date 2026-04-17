import base64
from pathlib import Path
import streamlit as st

st.set_page_config(
    page_title="Lindsey Lei | Portfolio",
    page_icon="🌿",
    layout="wide"
)

# -----------------------------
# Language
# -----------------------------
LANGS = ["English", "中文"]

TEXT = {
    "English": {
        "portfolio": "Portfolio",
        "explore": "Explore",
        "nav": ["Home", "About", "Experience", "Projects", "Fun Facts", "Skills", "Contact"],
        "location": "Location",
        "email": "Email",
        "linkedin": "LinkedIn",
        "home_chip": "Marketing · Analytics · AI Product",
        "home_subtitle": "Master of Management Analytics | University of Toronto",
        "home_intro": "I enjoy turning broad questions into structured analysis and translating complex work into decisions that feel clear, thoughtful, and useful.",
        "scroll": "Explore more",
        "about_label": "About",
        "about_title_home": "About my work",
        "about_body_home": "My background combines marketing, analytics, and AI-related product work. I’m especially interested in roles where data can shape decisions, products, and user experience.",
        "focus_label": "What I'm building toward",
        "focus_title": "What I’m building toward",
        "focus_items": [
            "Deepen my foundation in analytics, experimentation, and statistical thinking.",
            "Grow at the intersection of data, AI, and business strategy.",
            "Build toward roles where I can turn analysis into product and strategic impact.",
        ],
        "about_page_label": "About me",
        "about_page_title": "About me",
        "about_page_body_1": "As a debater and debate coach, I developed a strong foundation in structured thinking and clear reasoning. This way of approaching problems continues to shape how I communicate, analyze, and make decisions.",
        "about_page_body_2": "During my experience in marketing roles, I often worked closely with engineers and product teams. A recurring question I faced was: how do we know this actually works? I realized that while I could propose ideas, I could not always support them with rigorous evidence.",
        "about_page_body_3": "That gap led me to pursue data analytics and statistics more deeply. I wanted to move from intuition-driven decisions to evidence-based thinking, not just understanding what works, but why it works.",
        "about_page_body_4": "Today, my work sits at the intersection of analytics, business strategy, and AI. I am especially interested in using data to translate complex problems into clear insights, and turning those insights into decisions that are both practical and impactful.",
        "highlights_label": "What I bring",
        "highlights_title": "What I bring",
        "highlights_items": [
            "Turn business questions into structured, measurable analysis that supports better decisions.",
            "Translate data into clear insights and recommendations, not just technical outputs.",
            "Bridge business, product, and technical teams to keep work aligned and actionable.",
        ],
        "experience_label": "Experience",
        "experience_title": "Selected experience",
        "experience_filter": "Filter by area",
        "projects_label": "Projects",
        "projects_title": "Selected projects",
        "category": "Category",
        "skill_tag": "Skill / tag",
        "sort_by": "Sort by",
        "featured": "Featured",
        "latest": "Latest",
        "selected_work": "Selected work",
        "why_it_matters": "Why it matters",
        "project_links_label": "Links",
        "fun_facts_label": "Fun Facts",
        "fun_facts_title": "Beyond work",
        "skills_label": "Skills",
        "skills_title": "Tools and strengths",
        "contact_label": "Contact",
        "contact_title": "Let's connect",
        "contact_details": "Contact details",
        "notes": "Notes",
        "notes_body_1": "Open to conversations around analytics, AI product, product strategy, and data-driven decision making.",
        "notes_body_2": "Resume available upon request.",
        "analytics_technical": "Analytics & Technical",
        "business_product": "Business & Product",
        "no_experience": "No experience items match this filter yet.",
        "no_projects": "No projects match this filter combination.",
        "built_note": "Built with Streamlit. Visual direction inspired by soft green tones, light, and texture.",
        "language_label": "Language / 语言",
        "project_type_all": "All",
        "project_type_analytics": "Analytics",
        "project_type_ai_product": "AI / Product",
        "project_type_product": "Product",
        "experience_filter_options": ["All", "Analytics", "Marketing", "Product", "AI", "Growth", "Research"],
        "hero_name": "Lindsey Lei",
    },
    "中文": {
        "portfolio": "作品集",
        "explore": "浏览",
        "nav": ["主页", "关于我", "经历", "项目", "更多面向", "技能", "联系我"],
        "location": "地点",
        "email": "邮箱",
        "linkedin": "领英",
        "home_chip": "市场 · 分析 · AI 产品",
        "home_subtitle": "多伦多大学管理分析硕士",
        "home_intro": "我喜欢把宽泛的问题整理成清晰的分析框架，并把复杂的工作转化成更明确、更有思考感、也更有用的决策。",
        "scroll": "向下滑动查看",
        "about_label": "关于",
        "about_title_home": "我的工作方向",
        "about_body_home": "我的背景结合了市场、数据分析和 AI 相关产品工作。我尤其感兴趣的是那些能让数据真正影响决策、产品和用户体验的角色。",
        "focus_label": "我正在发展的方向",
        "focus_title": "我正在发展的方向",
        "focus_items": [
            "继续深化我在 analytics、实验设计和统计思维上的基础。",
            "在 data、AI 和 business strategy 的交叉点上持续成长。",
            "走向能把分析转化为产品和战略影响的岗位。",
        ],
        "about_page_label": "关于我",
        "about_page_title": "About me",
        "about_page_body_1": "作为辩手和辩论教练，我建立了比较扎实的结构化思考和清晰推理能力。这种处理问题的方式一直影响着我如何沟通、分析和做判断。",
        "about_page_body_2": "在做 marketing 相关工作时，我经常和工程师以及产品团队紧密合作。我反复会遇到一个问题：我们怎么知道这件事真的有效？我意识到，虽然我能提出想法，但我并不总能用足够严谨的证据去支持它。",
        "about_page_body_3": "这个 gap 让我更深入地去学习 data analytics 和 statistics。我想从依赖直觉的判断，走向更基于证据的思考方式，不只是知道什么有效，也知道为什么有效。",
        "about_page_body_4": "现在，我的工作兴趣主要在 analytics、business strategy 和 AI 的交叉点上。我尤其希望用数据把复杂问题翻译成清晰洞察，再把这些洞察转化成真正有实践价值的决策。",
        "highlights_label": "我能带来的东西",
        "highlights_title": "我能带来的东西",
        "highlights_items": [
            "把商业问题转化成结构化、可衡量的分析，支持更好的决策。",
            "把数据翻译成清晰的洞察和建议，而不只是技术输出。",
            "连接 business、product 和 technical 团队，让工作保持对齐并可执行。",
        ],
        "experience_label": "经历",
        "experience_title": "精选经历",
        "experience_filter": "按方向筛选",
        "projects_label": "项目",
        "projects_title": "精选项目",
        "category": "类别",
        "skill_tag": "技能 / 标签",
        "sort_by": "排序方式",
        "featured": "重点项目",
        "latest": "最新",
        "selected_work": "主要工作",
        "why_it_matters": "项目意义",
        "project_links_label": "相关链接",
        "fun_facts_label": "更多面向",
        "fun_facts_title": "工作之外",
        "skills_label": "技能",
        "skills_title": "工具与能力",
        "contact_label": "联系我",
        "contact_title": "欢迎联系",
        "contact_details": "联系方式",
        "notes": "说明",
        "notes_body_1": "欢迎交流与数据分析、AI 产品、产品策略和数据驱动决策相关的话题。",
        "notes_body_2": "简历可按需提供。",
        "analytics_technical": "分析与技术",
        "business_product": "商业与产品",
        "no_experience": "当前筛选下没有匹配的经历。",
        "no_projects": "当前筛选组合下没有匹配的项目。",
        "built_note": "Built with Streamlit. 整体视觉风格参考了柔和的绿色、光影和质感。",
        "language_label": "Language / 语言",
        "project_type_all": "全部",
        "project_type_analytics": "分析",
        "project_type_ai_product": "AI / 产品",
        "project_type_product": "产品",
        "experience_filter_options": ["全部", "分析", "市场", "产品", "AI", "增长", "研究"],
        "hero_name": "Lindsey Lei",
    }
}

# -----------------------------
# Project / experience data
# -----------------------------
projects = [
    {
        "title_en": "Galaxy",
        "title_zh": "Galaxy",
        "year": 2026,
        "type_key": "product",
        "featured": True,
        "tags": ["AI", "Product", "UX", "Behavior Design"],
        "subtitle_en": "AI-powered planning tool · Product vision · UX simplicity",
        "subtitle_zh": "AI 规划工具 · 产品愿景 · 简洁用户体验",
        "summary_en": "Led product vision and development direction for an AI-powered task management tool designed to convert abstract goals into structured action plans.",
        "summary_zh": "负责一款 AI 任务管理工具的产品方向与开发思路，帮助用户把抽象目标转化为结构化行动计划。",
        "details_en": [
            "Defined product direction and user value proposition",
            "Focused on reducing cognitive load through UX simplicity",
            "Worked on planning logic, user flow, and product structure",
        ],
        "details_zh": [
            "定义产品方向与用户价值主张",
            "通过简洁的体验设计降低用户的认知负担",
            "参与规划逻辑、用户流程和产品结构设计",
        ],
        "impact_en": "Reflects a product mindset grounded in both user behavior and practical execution.",
        "impact_zh": "体现了我将用户行为理解与实际产品落地结合起来的产品思维。",
        "links": [
            {"label": "Galaxy Pitch", "url": "https://canva.link/galaxypitch"},
            {"label": "Galaxy Prototype", "url": "https://www.figma.com/make/Pry7MhJoX7BgF1V3KAq7ip/ADHD-Planet-App-Overview?fullscreen=1"},
        ],
    },
    {
        "title_en": "Sound Based Emotion Detector",
        "title_zh": "基于声音的情绪识别模型",
        "year": 2025,
        "type_key": "ai_product",
        "featured": True,
        "tags": ["Python", "Audio", "Machine Learning", "Evaluation"],
        "subtitle_en": "Audio classification · Transfer learning · Model evaluation",
        "subtitle_zh": "音频分类 · 迁移学习 · 模型评估",
        "summary_en": "Developed an emotion classification model using audio inputs and evaluated performance across groups to assess model generalization.",
        "summary_zh": "基于音频输入构建情绪分类模型，并通过分组比较评估模型的泛化能力。",
        "details_en": [
            "Built an emotion classification workflow on sound-based data",
            "Applied transfer learning to improve model performance",
            "Compared results across demographic groups to assess generalization",
        ],
        "details_zh": [
            "在声音数据上搭建情绪分类流程",
            "应用迁移学习提升模型表现",
            "通过不同群体结果比较评估模型泛化能力",
        ],
        "impact_en": "Shows technical modeling ability alongside an awareness of evaluation quality and robustness.",
        "impact_zh": "既体现了建模能力，也体现了我对评估质量与模型稳健性的关注。",
        "links": [
            {"label": "Speech Deck", "url": "https://canva.link/czrb6kp64tpaeva"},
        ],
    },
    {
        "title_en": "L.O.V.E. Multi-Agent Relationship Support System",
        "title_zh": "L.O.V.E. 多智能体关系支持系统",
        "year": 2026,
        "type_key": "ai_product",
        "featured": True,
        "tags": ["LLM", "RAG", "Multi-Agent", "Evaluation", "Product"],
        "subtitle_en": "LLM agent · RAG · Routing · Structured actions · Memory",
        "subtitle_zh": "LLM 智能体 · RAG · 路由 · 结构化动作 · 记忆机制",
        "summary_en": "Built a structured multi-agent LLM system designed to support relationship-related conversations through retrieval, routing, action flows, and persistent memory.",
        "summary_zh": "构建了一个多智能体 LLM 系统，通过检索、路由、动作流程和记忆机制支持关系类对话场景。",
        "details_en": [
            "Helped design a RAG-based system grounded in therapist-informed knowledge",
            "Structured workflows for planning, reflection, and support actions",
            "Worked with evaluation dimensions such as retrieval, routing, safety, and action reliability",
            "Presented architecture and evaluation logic in a team setting",
        ],
        "details_zh": [
            "参与设计基于治疗知识的 RAG 系统结构",
            "梳理规划、反思和支持动作的工作流",
            "围绕检索、路由、安全性和动作可靠性进行评估设计",
            "在团队展示中讲解系统架构与评估逻辑",
        ],
        "impact_en": "Demonstrates the ability to work on AI products that combine system design, user needs, and evaluation thinking.",
        "impact_zh": "体现了我在 AI 产品中同时兼顾系统设计、用户需求与评估思维的能力。",
        "links": [
            {"label": "L.O.V.E. Pitch", "url": "https://canva.link/loveaiagent"},
            {"label": "Demo Video", "url": "https://www.youtube.com/watch?v=jEcYYLnz-lo"},
            {"label": "App Link", "url": "https://rsm8430-group18-mt3nu7g4geqgvsmfq97ikn.streamlit.app/"},
        ],
    },
    {
        "title_en": "Toronto Police Services Crime Risk Prediction",
        "title_zh": "多伦多警察局犯罪风险预测",
        "year": 2026,
        "type_key": "analytics",
        "featured": True,
        "tags": ["Python", "Machine Learning", "Public Sector", "Prediction"],
        "subtitle_en": "ML modeling · Risk prediction · Decision support",
        "subtitle_zh": "机器学习建模 · 风险预测 · 决策支持",
        "summary_en": "Built predictive models for location-level crime risk to support proactive deployment and operational decision-making for Toronto Police Services.",
        "summary_zh": "构建地点级别的犯罪风险预测模型，帮助多伦多警察局进行前瞻性的资源部署与运营决策。",
        "details_en": [
            "Worked on predictive modeling for risk estimation",
            "Focused on supporting proactive resource allocation decisions",
            "Contributed to a competition-winning analytics solution",
        ],
        "details_zh": [
            "参与风险估计的预测建模",
            "支持前瞻性的资源配置决策",
            "参与完成获奖的数据分析方案",
        ],
        "impact_en": "Highlights applied machine learning in a real decision-support context with public-sector relevance.",
        "impact_zh": "体现了机器学习在真实公共部门决策支持场景中的应用价值。",
        "links": [
            {"label": "TPS Risk Model", "url": "https://canva.link/tpsriskmodel"},
        ],
    },
    {
        "title_en": "Summer Home Recommender System",
        "title_zh": "Summer Home 推荐系统",
        "year": 2025,
        "type_key": "ai_product",
        "featured": False,
        "tags": ["Python", "Recommender System", "Web App", "Product"],
        "subtitle_en": "Recommendation engine · User preferences · Housing search",
        "subtitle_zh": "推荐系统 · 用户偏好 · 住房搜索",
        "summary_en": "Designed and developed a web-based recommendation system to match users with travel accommodations based on budget, preferences, and location.",
        "summary_zh": "设计并开发了一个网页推荐系统，根据预算、偏好和地点为用户匹配住宿选择。",
        "details_en": [
            "Built a recommendation workflow for summer home selection",
            "Matched users to properties using stated preferences and constraints",
            "Framed the tool as a more efficient decision-support experience",
        ],
        "details_zh": [
            "搭建夏季度假住宿推荐流程",
            "基于用户偏好与约束条件进行匹配",
            "把工具定位成更高效的决策支持体验",
        ],
        "impact_en": "Shows product-oriented problem solving using recommendation logic and user-centered design.",
        "impact_zh": "体现了我以用户为中心、用推荐逻辑解决实际问题的产品思路。",
    },
    {
        "title_en": "ESG and Financial Performance Analysis",
        "title_zh": "ESG 与财务表现分析",
        "year": 2025,
        "type_key": "analytics",
        "featured": False,
        "tags": ["EDA", "Finance", "Visualization", "Regression"],
        "subtitle_en": "EDA · Industry comparison · Visualization · Financial analysis",
        "subtitle_zh": "EDA · 行业比较 · 可视化 · 财务分析",
        "summary_en": "Studied ESG scores and firm-level financial variables across industries to understand distribution patterns and relationships with business performance indicators.",
        "summary_zh": "研究不同行业中的 ESG 分数与公司层面财务变量，理解其分布模式以及与业务表现指标之间的关系。",
        "details_en": [
            "Conducted EDA on ESG scores, ROA, leverage, and firm size",
            "Compared ESG distributions across Fama-French 12 industries",
            "Built presentation-ready plots and summary tables",
            "Interpreted how ESG varied across industries and firm characteristics",
        ],
        "details_zh": [
            "对 ESG、ROA、杠杆率和公司规模进行探索性分析",
            "比较 Fama-French 12 个行业中的 ESG 分布差异",
            "制作适合展示的图表和汇总表",
            "解释 ESG 在行业和公司特征层面的差异",
        ],
        "impact_en": "Highlights the ability to structure financial analysis and communicate findings clearly for business audiences.",
        "impact_zh": "体现了我组织财务分析并向商业受众清晰表达结果的能力。",
    },
]

experiences = [
    {
        "title_en": "Technical Standards and Safety Authority",
        "title_zh": "Technical Standards and Safety Authority",
        "role_en": "Data Analyst Intern",
        "role_zh": "数据分析实习生",
        "period": "Jan 2026 – Jul 2026",
        "tags_en": ["Analytics", "Python", "Tableau"],
        "tags_zh": ["分析", "Python", "Tableau"],
        "bullets_en": [
            "Built dashboard-based decision support for operational prioritization",
            "Engineered large-scale features from real inspection and maintenance data",
            "Worked on elevator risk modeling to support inspector allocation and risk-based prioritization",
            "Built an interactive Tableau dashboard for cross-functional stakeholders",
            "Connected business questions with structured analytical workflows",
        ],
        "bullets_zh": [
            "搭建面向运营优先级决策的可视化支持工具",
            "基于真实检查与维护数据完成大规模特征工程",
            "参与电梯风险建模，支持检查资源配置和风险优先级排序",
            "搭建 Tableau 交互式看板支持跨团队沟通",
            "把业务问题转化为结构化分析流程",
        ],
        "links": [
            {"label": "TSSA Pitch", "url": "https://canva.link/tssapitch"},
        ],
    },
    {
        "title_en": "Nemo Language Learning",
        "title_zh": "Nemo Language Learning",
        "role_en": "Marketing Analyst",
        "role_zh": "市场分析师",
        "period": "Aug 2024 – May 2025",
        "tags_en": ["Marketing", "Research", "Product"],
        "tags_zh": ["市场", "研究", "产品"],
        "bullets_en": [
            "Conducted user interviews and surveys to understand engagement drivers",
            "Turned behavioral insights into product improvement directions",
            "Used content experiments to increase average views from 400 to 1,000",
        ],
        "bullets_zh": [
            "通过用户访谈和问卷理解互动行为的驱动因素",
            "将行为洞察转化为产品改进方向",
            "通过内容实验把平均浏览量从 400 提升到 1000",
        ],
    },
    {
        "title_en": "IMS Group / AI Creativity Tool",
        "title_zh": "IMS Group / AI 创意工具",
        "role_en": "Marketing Intern",
        "role_zh": "市场实习生",
        "period": "May 2023 – Jul 2023",
        "tags_en": ["Marketing", "AI", "Growth"],
        "tags_zh": ["市场", "AI", "增长"],
        "bullets_en": [
            "Supported campaigns for a generative AI creativity product",
            "Used customer surveys and SWOT analysis to improve conversion",
            "Helped grow livestream viewership from 2,000 to 13,000",
        ],
        "bullets_zh": [
            "支持生成式 AI 创意产品的市场活动",
            "通过用户调研和 SWOT 分析提升转化",
            "帮助直播观看量从 2000 提升到 13000",
        ],
    },
]

fun_facts_en = [
    "📻 I previously hosted a children’s radio show for two years and organized offline audience events, which was one of my earliest experiences engaging with a real audience.",
    "🥊 I have been training in boxing for four years. It has been a consistent part of my routine outside of academics and work.",
    "🎙️ I produced a weekly lifestyle podcast in Chinese that ranked #1 on an emerging creators chart on a major platform.",
    "✍️ I have written online fiction and blogs in Chinese, and was able to monetize the content on a small scale.",
    "🎸 I have also worked on original music and performed with a band.",
    "🏳️‍🌈 I am actively involved in supporting LGBTQ+ communities, and currently manage the Instagram and LinkedIn accounts for Rotman Pride.",
    "🗣️ I have a strong background in Chinese debate, including competing in and coaching university-level teams in Canada.",
    "🎪 I served as president of a student alliance across 20+ universities, organizing large-scale events such as business competitions and music festivals.",
    "🌱 I have explored sustainability from a philosophical perspective, including work on the practical implications of vegetarianism.",
    "💸 In high school, I created and sold study notes, generating over 3,000 RMB in revenue.",
]

fun_facts_zh = [
    "📻 我曾连续两年主持儿童广播节目，也组织过线下听众见面活动，这是我最早与真实受众建立连接的经历之一。",
    "🥊 我练拳击已经四年了，它一直是我在学习和工作之外非常稳定的一部分。",
    "🎙️ 我做过一个中文生活类周播客，曾登上大型平台新锐榜第一名。",
    "✍️ 我写过中文网络小说和博客，也做过小规模变现。",
    "🎸 我也做过原创音乐，并和乐队一起演出过。",
    "🏳️‍🌈 我一直积极支持 LGBTQ+ 社群，目前也在运营 Rotman Pride 的 Instagram 和 LinkedIn 账号。",
    "🗣️ 我有比较深的中文辩论背景，既参加比赛，也做过大学辩论队教练。",
    "🎪 我曾担任一个覆盖 20 多所学校的学生联盟主席，组织过商业竞赛和音乐节等活动。",
    "🌱 我曾从哲学角度研究可持续性议题，包括素食主义在现实中的实践问题。",
    "💸 高中时我做过卖学习笔记的小生意，累计收入超过 3000 元人民币。",
]

skills_en = {
    "Analytics & Technical": [
        "Python", "R", "SQL", "Tableau", "Power BI", "Excel", "Streamlit"
    ],
    "Business & Product": [
        "Consumer Research", "A/B Testing", "Campaign Strategy",
        "Social Media Analytics", "Brand Positioning",
        "Product Thinking", "Cross-functional collaboration"
    ]
}

skills_zh = {
    "分析与技术": [
        "Python", "R", "SQL", "Tableau", "Power BI", "Excel", "Streamlit"
    ],
    "商业与产品": [
        "用户研究", "A/B Testing", "营销策略",
        "社交媒体分析", "品牌定位",
        "产品思维", "跨职能协作"
    ]
}

# -----------------------------
# Helpers
# -----------------------------
def get_base64_image(path_str: str):
    path = Path(path_str)
    if not path.exists():
        return None
    return base64.b64encode(path.read_bytes()).decode()

def render_tags(tags):
    return " ".join([f"<span class='tag'>{tag}</span>" for tag in tags])

def render_link_pills(links):
    return " ".join(
        [f"<a class='project-link' href='{link['url']}' target='_blank'>{link['label']}</a>" for link in links]
    )

def render_project_card(project, lang, T):
    title = project["title_en"] if lang == "English" else project["title_zh"]
    subtitle = project["subtitle_en"] if lang == "English" else project["subtitle_zh"]
    summary = project["summary_en"] if lang == "English" else project["summary_zh"]
    details = project["details_en"] if lang == "English" else project["details_zh"]
    impact = project["impact_en"] if lang == "English" else project["impact_zh"]

    type_map = {
        "analytics": T["project_type_analytics"],
        "ai_product": T["project_type_ai_product"],
        "product": T["project_type_product"],
    }
    details_html = "".join([f"<li>{item}</li>" for item in details])
    links_html = ""
    if project.get("links"):
        links_html = f"""
        <div class='project-meta-label'>{T['project_links_label']}</div>
        <div class='project-link-row'>{render_link_pills(project['links'])}</div>
        """

    st.markdown(
        f"""
        <div class='project-card'>
            <div class='section-label'>{type_map[project['type_key']]} · {project['year']}</div>
            <h3>{title}</h3>
            <div class='card-subtitle'>{subtitle}</div>
            <p>{summary}</p>
            <div>{render_tags(project["tags"])}</div>
            <div class='project-meta-label'>{T['selected_work']}</div>
            <ul class='card-list'>{details_html}</ul>
            <div class='project-meta-label'>{T['why_it_matters']}</div>
            <p>{impact}</p>
            {links_html}
        </div>
        """,
        unsafe_allow_html=True,
    )

def render_experience_card(exp, lang, T):
    title = exp["title_en"] if lang == "English" else exp["title_zh"]
    role = exp["role_en"] if lang == "English" else exp["role_zh"]
    tags = exp["tags_en"] if lang == "English" else exp["tags_zh"]
    bullets = exp["bullets_en"] if lang == "English" else exp["bullets_zh"]
    bullets_html = "".join([f"<li>{bullet}</li>" for bullet in bullets])
    links_html = ""
    if exp.get("links"):
        links_html = f"""
        <div class='project-meta-label'>{T['project_links_label']}</div>
        <div class='project-link-row'>{render_link_pills(exp['links'])}</div>
        """
    st.markdown(
        f"""
        <div class='soft-card'>
            <div class='section-label'>{exp['period']}</div>
            <h3>{title}</h3>
            <div class='card-role'>{role}</div>
            <div>{render_tags(tags)}</div>
            <ul class='card-list'>{bullets_html}</ul>
            {links_html}
        </div>
        """,
        unsafe_allow_html=True,
    )

hero_image_base64 = get_base64_image("hero.jpg")
profile_image_base64 = get_base64_image("profile.jpg")

# -----------------------------
# Styling
# -----------------------------
hero_css = ""
if hero_image_base64:
    hero_css = f"""
    .home-hero {{
        width: 100%;
        min-height: 88vh;
        border-radius: 32px;
        overflow: hidden;
        position: relative;
        background-image:
            linear-gradient(180deg, rgba(247,246,241,0.10) 0%, rgba(247,246,241,0.18) 35%, rgba(247,246,241,0.70) 78%, rgba(247,246,241,0.90) 100%),
            url("data:image/jpeg;base64,{hero_image_base64}");
        background-size: cover;
        background-position: center;
        border: 1px solid rgba(89, 111, 92, 0.10);
        box-shadow: 0 14px 36px rgba(65, 80, 68, 0.06);
        display: flex;
        align-items: flex-end;
        margin-bottom: 0;
    }}
    .home-overlay {{
        width: 100%;
        min-height: 88vh;
        padding: 2.8rem 2.1rem 3.2rem 2.1rem;
        display: flex;
        flex-direction: column;
        justify-content: flex-end;
        position: relative;
    }}
    """
else:
    hero_css = """
    .home-hero {
        width: 100%;
        min-height: 88vh;
        border-radius: 32px;
        overflow: hidden;
        background: linear-gradient(135deg, rgba(255,255,255,0.88), rgba(227,238,228,0.74));
        border: 1px solid rgba(89, 111, 92, 0.10);
        box-shadow: 0 14px 36px rgba(65, 80, 68, 0.06);
        display: flex;
        align-items: flex-end;
        margin-bottom: 0;
    }
    .home-overlay {
        width: 100%;
        min-height: 88vh;
        padding: 2.8rem 2.1rem 3.2rem 2.1rem;
        display: flex;
        flex-direction: column;
        justify-content: flex-end;
        position: relative;
    }
    """

st.markdown(f"""
<style>
:root {{
    --bg: #f7f6f1;
    --bg2: #eef2ee;
    --card: rgba(255,255,255,0.82);
    --line: rgba(89, 111, 92, 0.10);
    --text: #33413a;
    --muted: #6e7b72;
    --sidebar-text: #445148;
    --link: #5c84a4;
    --pill-bg: #edf3ed;
    --pill-text: #49604f;
}}

html, body, [class*="css"] {{
    color: var(--text);
}}

.stApp {{
    background: linear-gradient(180deg, var(--bg) 0%, #f5f4ee 45%, var(--bg2) 100%);
    color: var(--text);
}}

.block-container {{
    max-width: 1120px;
    padding-top: 6.2rem;
    padding-bottom: 3rem;
}}

header[data-testid="stHeader"] {{
    background: rgba(247, 246, 241, 0.72);
    backdrop-filter: blur(6px);
    z-index: 10;
}}

[data-testid="stToolbar"] {{
    right: 1rem;
}}

section[data-testid="stSidebar"] {{
    background: #f7f6f1;
    border-right: 1px solid rgba(120, 140, 120, 0.10);
    display: none;
}}

section[data-testid="stSidebar"] * {{
    color: var(--sidebar-text) !important;
}}

section[data-testid="stSidebar"] a {{
    color: var(--link) !important;
    text-decoration: none;
}}

section[data-testid="stSidebar"] a:hover {{
    text-decoration: underline;
}}

section[data-testid="stSidebar"] .stRadio label {{
    color: var(--sidebar-text) !important;
    opacity: 1 !important;
}}

h1, h2, h3, h4 {{
    color: var(--text) !important;
    font-family: -apple-system, BlinkMacSystemFont, "SF Pro Display", sans-serif;
    letter-spacing: -0.01em;
}}

p, li, div, span, label {{
    color: var(--text);
}}

.soft-card {{
    padding: 1.35rem 1.3rem;
    border-radius: 22px;
    background: rgba(255,255,255,0.76);
    border: 1px solid var(--line);
    box-shadow: 0 8px 24px rgba(65, 80, 68, 0.04);
    margin-bottom: 1rem;
    display: block;
    width: 100%;
    box-sizing: border-box;
}}

.project-card {{
    padding: 1.4rem 1.4rem 1.15rem 1.4rem;
    border-radius: 24px;
    background: rgba(255,255,255,0.80);
    border: 1px solid var(--line);
    box-shadow: 0 8px 24px rgba(65, 80, 68, 0.04);
    margin-bottom: 1rem;
    display: block;
    width: 100%;
    box-sizing: border-box;
}}

.section-label {{
    font-size: 0.84rem;
    text-transform: uppercase;
    letter-spacing: 0.14em;
    color: var(--muted) !important;
    margin-bottom: 0.45rem;
}}

.tag {{
    display: inline-block;
    padding: 0.28rem 0.62rem;
    margin: 0.15rem 0.3rem 0.15rem 0;
    border-radius: 999px;
    background: var(--pill-bg);
    border: 1px solid rgba(125, 149, 128, 0.14);
    color: var(--pill-text) !important;
    font-size: 0.82rem;
}}

.small-note {{
    color: var(--muted) !important;
    font-size: 0.9rem;
    margin-top: 0.25rem;
}}

.topbar-shell {{
    position: fixed;
    top: 0.9rem;
    left: 50%;
    transform: translateX(-50%);
    z-index: 1005;
    width: min(1120px, calc(100vw - 2rem));
    pointer-events: none;
}}

.topbar {{
    display: flex;
    align-items: center;
    justify-content: space-between;
    gap: 1rem;
    padding: 0.95rem 1.15rem;
    border-radius: 22px;
    background: rgba(248, 247, 242, 0.96);
    border: 1px solid rgba(79, 97, 82, 0.18);
    backdrop-filter: blur(14px);
    box-shadow: 0 12px 34px rgba(65, 80, 68, 0.12);
    pointer-events: auto;
}}

.topbar,
.topbar * {{
    opacity: 1 !important;
    visibility: visible !important;
}}

.brand-mark {{
    font-size: 0.98rem;
    font-weight: 700;
    letter-spacing: 0.08em;
    text-transform: uppercase;
    color: #26342b !important;
    white-space: nowrap;
}}

.topnav {{
    display: flex;
    align-items: center;
    justify-content: flex-end;
    gap: 0.5rem;
    flex-wrap: wrap;
    min-width: 0;
}}

.topnav a {{
    display: inline-flex;
    align-items: center;
    justify-content: center;
    padding: 0.48rem 0.82rem;
    border-radius: 999px;
    color: #314137 !important;
    text-decoration: none;
    font-size: 0.94rem;
    font-weight: 600;
    line-height: 1;
    background: rgba(255,255,255,0.62);
    border: 1px solid rgba(89, 111, 92, 0.10);
    transition: background 0.18s ease, color 0.18s ease, border-color 0.18s ease;
}}

.topnav a:hover {{
    background: rgba(255,255,255,0.96);
    border-color: rgba(89, 111, 92, 0.22);
    color: #223128 !important;
}}

.hero-chip {{
    display: inline-block;
    padding: 0.38rem 0.78rem;
    border-radius: 999px;
    background: rgba(255,255,255,0.72);
    border: 1px solid rgba(89,111,92,0.10);
    color: #53665a !important;
    font-size: 0.82rem;
    letter-spacing: 0.08em;
    text-transform: uppercase;
    margin-bottom: 1rem;
}}

.home-title {{
    font-size: 4.2rem;
    font-weight: 700;
    line-height: 1.02;
    color: #2f3e34 !important;
    margin-bottom: 0.6rem;
}}

.home-subtitle {{
    font-size: 1.35rem;
    font-weight: 550;
    color: #3a4a41 !important;
    margin-bottom: 1rem;
}}

.hero-note {{
    color: #425148 !important;
    font-size: 1.04rem;
    line-height: 1.75;
    max-width: 760px;
}}

.hero-copy {{
    max-width: 760px;
}}

.scroll-note {{
    position: absolute;
    left: 50%;
    bottom: 1.25rem;
    transform: translateX(-50%);
    display: flex;
    flex-direction: column;
    align-items: center;
    gap: 0.32rem;
    font-size: 0.92rem;
    color: var(--muted) !important;
    letter-spacing: 0.06em;
    text-transform: uppercase;
    text-align: center;
}}

.scroll-arrow {{
    display: inline-block;
    font-size: 1.15rem;
    line-height: 1;
    animation: floatDown 1.7s ease-in-out infinite;
}}

@keyframes floatDown {{
    0%, 100% {{
        transform: translateY(0);
        opacity: 0.7;
    }}
    50% {{
        transform: translateY(7px);
        opacity: 1;
    }}
}}

.home-section-gap {{
    height: 3.6rem;
}}

.anchor-section {{
    scroll-margin-top: 7.5rem;
}}

.home-stage {{
    min-height: calc(100vh - 6.8rem);
    display: flex;
    align-items: stretch;
    width: 100%;
}}

.about-card {{
    min-height: 260px;
}}

.about-story {{
    padding: 0.6rem 0 1rem 0;
    margin-bottom: 1.5rem;
}}

.about-grid {{
    display: grid;
    grid-template-columns: 240px minmax(0, 1fr);
    gap: 2rem;
    align-items: start;
}}

.about-photo-wrap {{
    display: flex;
    justify-content: center;
}}

.about-photo {{
    width: 220px;
    height: 220px;
    border-radius: 50%;
    overflow: hidden;
    border: 8px solid rgba(255,255,255,0.82);
    box-shadow: 0 16px 36px rgba(65, 80, 68, 0.12);
    background: linear-gradient(180deg, rgba(227,239,228,0.96) 0%, rgba(214,231,216,0.96) 100%);
    flex: 0 0 auto;
}}

.about-photo img {{
    width: 100%;
    height: 100%;
    object-fit: cover;
    display: block;
}}

.about-photo-fallback {{
    width: 100%;
    height: 100%;
    display: flex;
    align-items: center;
    justify-content: center;
    font-size: 2.6rem;
    font-weight: 700;
    color: #314137 !important;
    letter-spacing: 0.04em;
}}

.about-copy {{
    min-width: 0;
}}

.about-story p {{
    font-size: 1.08rem;
    line-height: 1.9;
    margin-bottom: 1rem;
}}

.green-card {{
    padding: 1.5rem 1.4rem 1.35rem 1.4rem;
    border-radius: 26px;
    background: linear-gradient(180deg, rgba(227,239,228,0.96) 0%, rgba(214,231,216,0.96) 100%);
    border: 1px solid rgba(104, 133, 107, 0.16);
    box-shadow: 0 12px 26px rgba(92, 118, 95, 0.08);
    min-height: 100%;
    height: 100%;
    display: block;
    width: 100%;
    box-sizing: border-box;
}}

.green-card h3,
.green-card .section-label,
.green-card li,
.green-card p {{
    color: #314137 !important;
}}

.green-card ul {{
    margin: 0.4rem 0 0 1.1rem;
    padding: 0;
}}

.green-card li {{
    margin-bottom: 0.8rem;
    line-height: 1.7;
}}

.card-subtitle {{
    color: var(--muted) !important;
    font-size: 0.95rem;
    margin: -0.15rem 0 0.7rem 0;
}}

.card-role {{
    font-weight: 600;
    margin-bottom: 0.7rem;
    color: #304037 !important;
}}

.card-list {{
    margin: 0.65rem 0 0 1.1rem;
    padding: 0;
}}

.card-list li {{
    margin-bottom: 0.72rem;
    line-height: 1.7;
}}

.project-meta-label {{
    font-weight: 700;
    margin-top: 0.9rem;
    margin-bottom: 0.35rem;
    color: #314137 !important;
}}

.project-link-row {{
    display: flex;
    flex-wrap: wrap;
    gap: 0.55rem;
    margin-top: 0.4rem;
}}

.project-link {{
    display: inline-flex;
    align-items: center;
    justify-content: center;
    padding: 0.48rem 0.82rem;
    border-radius: 999px;
    background: rgba(230, 239, 230, 0.95);
    border: 1px solid rgba(104, 133, 107, 0.18);
    color: #2f4235 !important;
    text-decoration: none;
    font-size: 0.9rem;
    font-weight: 600;
}}

.project-link:hover {{
    background: rgba(220, 234, 221, 1);
    border-color: rgba(104, 133, 107, 0.28);
}}

{hero_css}

div[data-baseweb="select"] > div,
.stSelectbox div[data-baseweb="select"] > div {{
    background: rgba(255,255,255,0.96) !important;
    border: 1px solid rgba(120, 140, 120, 0.16) !important;
    border-radius: 14px;
    color: var(--text) !important;
    box-shadow: 0 8px 22px rgba(65, 80, 68, 0.06);
}}

div[data-baseweb="select"] input,
.stSelectbox input,
div[data-baseweb="select"] span,
.stSelectbox div[data-baseweb="select"] span {{
    color: var(--text) !important;
    -webkit-text-fill-color: var(--text) !important;
}}

div[data-baseweb="popover"] ul,
div[role="listbox"] {{
    background: rgba(252, 251, 247, 0.98) !important;
    border: 1px solid rgba(120, 140, 120, 0.16) !important;
    border-radius: 16px !important;
    box-shadow: 0 14px 28px rgba(65, 80, 68, 0.10) !important;
}}

div[data-baseweb="popover"] li,
div[role="option"] {{
    background: transparent !important;
    color: var(--text) !important;
}}

div[data-baseweb="popover"] li:hover,
div[role="option"]:hover {{
    background: #edf3ed !important;
    color: #2d3c33 !important;
}}

div[aria-selected="true"] {{
    background: #e4eee4 !important;
    color: #243229 !important;
}}

.stButton button, .stDownloadButton button {{
    border-radius: 14px;
    border: 1px solid rgba(120, 140, 120, 0.12);
    background: #eef4ee;
    color: var(--text) !important;
}}

.stButton button:hover, .stDownloadButton button:hover {{
    border-color: rgba(120, 140, 120, 0.24);
    background: #e4eee4;
}}

hr {{
    border: none;
    border-top: 1px solid rgba(120, 140, 120, 0.10);
    margin-top: 1.2rem;
    margin-bottom: 1.2rem;
}}

.stRadio [role="radiogroup"] {{
    gap: 0.35rem;
}}

.element-container:has(> div.stRadio) {{
    position: fixed;
    top: 1.2rem;
    right: max(calc((100vw - 1120px) / 2 + 1rem), 1rem);
    z-index: 1001;
    margin: 0;
}}

.element-container:has(> div.stRadio) .stRadio {{
    padding: 0.2rem 0.3rem;
    background: rgba(247, 246, 241, 0.92);
    border: 1px solid rgba(89, 111, 92, 0.12);
    border-radius: 999px;
    box-shadow: 0 10px 24px rgba(65, 80, 68, 0.06);
}}

.stRadio [role="radiogroup"] label {{
    background: transparent;
    border: 1px solid transparent;
    border-radius: 999px;
    padding: 0.18rem 0.7rem;
}}

@media (max-width: 900px) {{
    .block-container {{
        padding-top: 7.4rem;
    }}

    .topbar {{
        border-radius: 28px;
        align-items: stretch;
        flex-direction: column;
        padding: 0.95rem;
    }}

    .brand-mark {{
        font-size: 0.9rem;
    }}

    .topnav {{
        justify-content: flex-start;
        width: 100%;
        flex-wrap: nowrap;
        overflow-x: auto;
        overflow-y: hidden;
        padding-bottom: 0.2rem;
        -webkit-overflow-scrolling: touch;
        scrollbar-width: none;
    }}

    .topnav::-webkit-scrollbar {{
        display: none;
    }}

    .topnav a {{
        flex: 0 0 auto;
    }}

    .element-container:has(> div.stRadio) {{
        top: 5.4rem;
        right: 1rem;
    }}

    .home-title {{
        font-size: 3.1rem;
    }}

    .home-subtitle {{
        font-size: 1.08rem;
    }}

    .home-stage {{
        min-height: calc(100vh - 8.6rem);
    }}

    .home-overlay {{
        min-height: 80vh;
        padding: 2rem 1.35rem 3.7rem 1.35rem;
    }}

    .scroll-note {{
        bottom: 1rem;
        font-size: 0.82rem;
    }}

    .about-grid {{
        grid-template-columns: 1fr;
        gap: 1.35rem;
    }}

    .about-photo-wrap {{
        justify-content: flex-start;
    }}

    .about-photo {{
        width: 180px;
        height: 180px;
    }}
}}
</style>
""", unsafe_allow_html=True)

# -----------------------------
# Top controls
# -----------------------------
language = st.radio(
    TEXT["English"]["language_label"],
    LANGS,
    horizontal=True,
    label_visibility="collapsed",
)

T = TEXT[language]
nav_ids = ["home", "about", "experience", "projects", "fun", "skills", "contact"]
nav_links = "".join(
    [f"<a href='#{section_id}'>{label}</a>" for label, section_id in zip(T["nav"], nav_ids)]
)

st.markdown(
    f"""
    <div class="topbar-shell">
        <div class="topbar">
            <div class="brand-mark">Lindsey Lei</div>
            <div class="topnav">{nav_links}</div>
        </div>
    </div>
    """,
    unsafe_allow_html=True,
)

# -----------------------------
# Single-page layout
# -----------------------------
st.markdown("<div id='home' class='anchor-section'></div>", unsafe_allow_html=True)
st.markdown(
    f"""
    <div class="home-stage">
        <div class="home-hero">
            <div class="home-overlay">
                <div class="hero-copy">
                    <div class="hero-chip">{T['home_chip']}</div>
                    <div class="home-title">{T['hero_name']}</div>
                    <div class="home-subtitle">{T['home_subtitle']}</div>
                    <div class="hero-note">
                        {T['home_intro']}
                    </div>
                </div>
                <div class="scroll-note">
                    <span>{T['scroll']}</span>
                    <span class="scroll-arrow">↓</span>
                </div>
            </div>
        </div>
    </div>
    """,
    unsafe_allow_html=True,
)

st.markdown("<div class='home-section-gap'></div>", unsafe_allow_html=True)

st.markdown("<div id='about' class='anchor-section'></div>", unsafe_allow_html=True)
profile_markup = (
    f"<img src='data:image/jpeg;base64,{profile_image_base64}' alt='Lindsey Lei portrait' />"
    if profile_image_base64
    else "<div class='about-photo-fallback'>LL</div>"
)

st.markdown(
    f"""
    <div class='about-story'>
        <div class='about-grid'>
            <div class='about-photo-wrap'>
                <div class='about-photo'>
                    {profile_markup}
                </div>
            </div>
            <div class='about-copy'>
                <div class='section-label'>{T['about_page_label']}</div>
                <h2>{T['about_page_title']}</h2>
                <p>{T['about_page_body_1']}</p>
                <p>{T['about_page_body_2']}</p>
                <p>{T['about_page_body_3']}</p>
                <p>{T['about_page_body_4']}</p>
            </div>
        </div>
    </div>
    """,
    unsafe_allow_html=True,
)

about_bottom_left, about_bottom_right = st.columns(2, gap="large")

with about_bottom_left:
    highlights_html = "".join([f"<li>{item}</li>" for item in T["highlights_items"]])
    st.markdown(
        f"""
        <div class='green-card'>
            <div class='section-label'>{T['highlights_label']}</div>
            <h3>{T['highlights_title']}</h3>
            <ul>{highlights_html}</ul>
        </div>
        """,
        unsafe_allow_html=True,
    )

with about_bottom_right:
    focus_html = "".join([f"<li>{item}</li>" for item in T["focus_items"]])
    st.markdown(
        f"""
        <div class='green-card'>
            <div class='section-label'>{T['focus_label']}</div>
            <h3>{T['focus_title']}</h3>
            <ul>{focus_html}</ul>
        </div>
        """,
        unsafe_allow_html=True,
    )

st.markdown("<div class='home-section-gap'></div>", unsafe_allow_html=True)

st.markdown("<div id='experience' class='anchor-section'></div>", unsafe_allow_html=True)
st.markdown(f"<div class='section-label'>{T['experience_label']}</div>", unsafe_allow_html=True)
st.markdown(f"## {T['experience_title']}")

exp_options = T["experience_filter_options"]
exp_filter = st.selectbox(T["experience_filter"], exp_options)

shown = 0
for exp in experiences:
    tags = exp["tags_en"] if language == "English" else exp["tags_zh"]
    all_label = "All" if language == "English" else "全部"
    if exp_filter == all_label or exp_filter in tags:
        render_experience_card(exp, language, T)
        shown += 1

if shown == 0:
    st.info(T["no_experience"])

st.markdown("<div class='home-section-gap'></div>", unsafe_allow_html=True)

st.markdown("<div id='projects' class='anchor-section'></div>", unsafe_allow_html=True)
st.markdown(f"<div class='section-label'>{T['projects_label']}</div>", unsafe_allow_html=True)
st.markdown(f"## {T['projects_title']}")

col1, col2, col3 = st.columns([1.1, 1, 1.1], gap="medium")
type_options = [
    T["project_type_all"],
    T["project_type_analytics"],
    T["project_type_ai_product"],
    T["project_type_product"],
]

with col1:
    type_filter = st.selectbox(T["category"], type_options)
with col2:
    tag_filter = st.selectbox(T["skill_tag"], [T["project_type_all"]] + sorted({tag for p in projects for tag in p["tags"]}))
with col3:
    sort_by = st.selectbox(T["sort_by"], [T["featured"], T["latest"]])

filtered = projects.copy()

if type_filter != T["project_type_all"]:
    reverse_type_map = {
        T["project_type_analytics"]: "analytics",
        T["project_type_ai_product"]: "ai_product",
        T["project_type_product"]: "product",
    }
    filtered = [p for p in filtered if p["type_key"] == reverse_type_map[type_filter]]

if tag_filter != T["project_type_all"]:
    filtered = [p for p in filtered if tag_filter in p["tags"]]

if sort_by == T["latest"]:
    filtered = sorted(filtered, key=lambda x: x["year"], reverse=True)
else:
    filtered = sorted(filtered, key=lambda x: (x["featured"], x["year"]), reverse=True)

if not filtered:
    st.info(T["no_projects"])
else:
    for project in filtered:
        render_project_card(project, language, T)

st.markdown("<div class='home-section-gap'></div>", unsafe_allow_html=True)

st.markdown("<div id='fun' class='anchor-section'></div>", unsafe_allow_html=True)
st.markdown(f"<div class='section-label'>{T['fun_facts_label']}</div>", unsafe_allow_html=True)
st.markdown(f"## {T['fun_facts_title']}")

facts = fun_facts_en if language == "English" else fun_facts_zh
col1, col2 = st.columns(2, gap="large")
left_items = facts[:5]
right_items = facts[5:]

with col1:
    left_facts_html = "".join([f"<li>{item}</li>" for item in left_items])
    st.markdown(
        f"""
        <div class='soft-card'>
            <ul class='card-list'>{left_facts_html}</ul>
        </div>
        """,
        unsafe_allow_html=True,
    )

with col2:
    right_facts_html = "".join([f"<li>{item}</li>" for item in right_items])
    st.markdown(
        f"""
        <div class='soft-card'>
            <ul class='card-list'>{right_facts_html}</ul>
        </div>
        """,
        unsafe_allow_html=True,
    )

st.markdown("<div class='home-section-gap'></div>", unsafe_allow_html=True)

st.markdown("<div id='skills' class='anchor-section'></div>", unsafe_allow_html=True)
st.markdown(f"<div class='section-label'>{T['skills_label']}</div>", unsafe_allow_html=True)
st.markdown(f"## {T['skills_title']}")

skill_pack = skills_en if language == "English" else skills_zh
skill_keys = list(skill_pack.keys())

s1, s2 = st.columns(2, gap="large")

with s1:
    st.markdown(
        f"""
        <div class='soft-card'>
            <h3>{skill_keys[0]}</h3>
            <div>{render_tags(skill_pack[skill_keys[0]])}</div>
        </div>
        """,
        unsafe_allow_html=True,
    )

with s2:
    st.markdown(
        f"""
        <div class='soft-card'>
            <h3>{skill_keys[1]}</h3>
            <div>{render_tags(skill_pack[skill_keys[1]])}</div>
        </div>
        """,
        unsafe_allow_html=True,
    )

st.markdown("<div class='home-section-gap'></div>", unsafe_allow_html=True)

st.markdown("<div id='contact' class='anchor-section'></div>", unsafe_allow_html=True)
st.markdown(f"<div class='section-label'>{T['contact_label']}</div>", unsafe_allow_html=True)
st.markdown(f"## {T['contact_title']}")

contact_html = f"""
<div class='soft-card'>
    <h3>{T['contact_details']}</h3>
    <div class='project-meta-label'>{T['email']}</div>
    <p>lindsey.lei@rotman.utoronto.ca</p>
    <div class='project-meta-label'>{T['linkedin']}</div>
    <p><a href='https://linkedin.com/in/lindsey-ranshuo-lei' target='_blank'>linkedin.com/in/lindsey-ranshuo-lei</a></p>
    <div class='project-meta-label'>{T['location']}</div>
    <p>Toronto, ON</p>
</div>
"""
st.markdown(contact_html, unsafe_allow_html=True)
