
import streamlit as st

st.set_page_config(
    page_title="JPI Labs | AI & Employability",
    page_icon="✳",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# CUSTOM CSS
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=DM+Sans:wght@400;500;600;700;800&family=Playfair+Display:wght@600;700&display=swap');

.stApp {
    background-color: #F7F6F2;
    color: #182B49;
    font-family: 'DM Sans', sans-serif;
}

.block-container {
    max-width: 1200px;
    padding-top: 1rem;
    padding-bottom: 2rem;
}

[data-testid="stVerticalBlock"] {
    gap: 0.5rem;
}

header, footer, #MainMenu {
    visibility: hidden;
}

.hero {
    padding: 42px 30px 40px 30px;
    background: #182B49;
    color: #F7F6F2;
    border-radius: 4px;
    margin-top: 12px;
}

.eyebrow {
    color: #E6A15C;
    text-transform: uppercase;
    letter-spacing: 3px;
    font-size: 13px;
    font-weight: 700;
}

.hero h1 {
    color: #F7F6F2;
    font-family: 'Playfair Display', serif;
    font-size: 66px;
    line-height: 1.12;
    margin: 25px 0;
}

.hero p {
    font-size: 19px;
    color: #D8DFE8;
    max-width: 650px;
    line-height: 1.8;
}

.section-label {
    color: #C17B37;
    text-transform: uppercase;
    letter-spacing: 2px;
    font-size: 18px;
    font-weight: 800;
}

h2 {
    font-family: 'Playfair Display', serif !important;
    color: #182B49 !important;
}

.info-card {
    background: #FFFFFF;
    border: 1px solid #E7E4DC;
    padding: 28px;
    min-height: 190px;
    border-radius: 5px;
}

.info-card h3 {
    color: #182B49;
    font-size: 21px;
}

.info-card p {
    color: #626B77;
    line-height: 1.7;
}

.navline {
    display: flex;
    justify-content: space-between;
    align-items: center;
    padding: 12px 0;
    border-bottom: 1px solid #DCD9D0;
}

.brand {
    font-weight: 800;
    font-size: 24px;
    letter-spacing: -1px;
    color: #182B49;
}

footer {
    color: #777;
}

[data-testid="stExpander"] {
    background: #FFFFFF;
    border: 1px solid #E7E4DC;
    border-radius: 5px;
    margin-bottom: 12px;
}

[data-testid="stExpander"] > details {
    min-height: 72px;
}

[data-testid="stExpander"] summary {
    min-height: 72px;
    padding: 20px 24px;
    color: #182B49;
    font-family: 'Playfair Display', serif;
    font-size: 38px;
    font-weight: 800;
}

[data-testid="stExpander"] [data-testid="stMarkdownContainer"] p {
    color: #626B77;
    line-height: 1.7;
}
</style>
""", unsafe_allow_html=True)


# NAVIGATION
st.markdown("""
<div class="navline">
    <div class="brand">✳ JPI LABS</div>
    <div style="color:#626B77;font-size:13px;">
""", unsafe_allow_html=True)


# HERO
st.markdown("""
<div class="hero">
    <h1>Empowering Students<br>in the Age of AI.</h1>
    <p>
        Exploring how artificial intelligence can reshape
        the relationship between education, professional
        development and the future of work.
    </p>
</div>
""", unsafe_allow_html=True)


# INTRODUCTION
st.markdown("""
<div class="section-label" style="margin-top:28px;">ABOUT THE PROJECT</div>
<p style="font-size:17px;line-height:1.9;color:#626B77;max-width:850px;">
Our project explores the practical applications of artificial
intelligence in student employability. Our project examines
how emerging AI technologies can help students navigate
recruitment, develop professional skills and make informed
career decisions.
</p>
""", unsafe_allow_html=True)


# AREAS OF WORK

# PROJECT AREAS

st.markdown('<div class="section-label" style="margin-top:32px;margin-bottom:18px;">PROJECT AREAS</div>', unsafe_allow_html=True)

sections = [
    (
        "AI Literacy and Its Impact on the Job Market",
        """
### How are AI models built?

Large Language Models (LLMs) are versatile models capable of processing natural language and generating coherent responses to various prompts (Hou et al., 2024). LLMs are primarily trained using sizeable datasets and can perform tasks like text generation, language translation, and question answering (Shao et al., 2024). Beyond these individual tasks, AI-based tools can integrate multiple capabilities into a single workflow and, by extension, combine them to handle complex and multi-step tasks. LLMs can be subjected to instruction tuning, a process that involves the use of instruction–response examples to improve their ability to follow user directives. The efficacy of this process partly depends on the quality, diversity, and complexity of the training data. Additionally, advanced techniques such as reinforcement learning from human feedback can further align model outputs with human preferences (Zhang et al., 2026).

### AI in the Academic Field

Unequivocally, the rather rapid development of AI models has exerted a great influence on academic components, particularly students. In recent years, an increasing number of students have been using AI tools primarily to improve their academic writing and write computer code.

For instance, around 94% of university students say they use generative AI to help with assessed work, and over two-thirds of them maintain that AI skills are essential to building a strong career (Freeman, 2025). Other than academic support, university students employ AI tools to enhance their competitiveness in the job market, especially when applying for part-time jobs and internships. On the contrary, only 48% of teaching staff reported that they would be willing to help students to develop these skills for their future careers, which signifies the presence of institutional lags (Freeman, 2025). Moreover, university students in Arts and Humanities degrees are more likely to feel under-supported (Freeman, 2025). Therefore, these findings reinforce the idea that future generations should be AI literate, specifically when in pursuit of promising career opportunities.

### AI and Career Opportunities

AI tools can support university students when applying for career opportunities in multitudinous ways. In this context, utilising AI models would assist students in presenting their qualifications more effectively and adapting their applications to employers’ expectations. For example, AI can suggest improvements to the structure or wording of CVs, adapt motivation letters to a specific role, and generate exemplary interview questions for practice.

According to a field experiment conducted at the two largest universities in the Netherlands, LLMs enhance the quality of signals, particularly benefiting lower-quality applicants (Abbas Nejad et al., 2025), which certifies the effectiveness of AI tools in navigating career opportunities. Nonetheless, these improvements do not necessarily lead to increased interview invitations since AI improvements are “concentrated in (...) less influential sections of the cover letters” (Abbas Nejad et al., 2025). Moreover, LLMs reduce signal informativeness, and irresponsible AI use in job applications may lead to standardised CVs, making it harder for employers to distinguish candidates' actual abilities, which potentially leads to increased inefficiencies in labor market matching (Abbas Nejad et al., 2025). Thus, it is apparent that using unregulated AI-generated application materials poses numerous risks for students. In light of this, such materials should be cautiously reviewed to ensure that they adequately convey candidates’ skills and experiences rather than yielding skewed or exaggerated resumes.

Hence, AI literacy is essential to use AI reasonably and responsibly when preparing applications for the job market. Higher education remains a perfect medium where students could be responsibly educated on generative AI adoption for career readiness. In this respect, higher education institutions should better prepare students for career job opportunities by equipping them with the skills required to successfully work with AI and automation (Ganguli, 2025).

### Workshop Procedure

Given the vast and permanent influence of AI tools on the job market, our project chiefly aims to integrate multiple skills into AI models to create a useful tool for university students when applying for career opportunities. To achieve this, AI literacy workshops could be hosted to inform university students about how AI should assist them when applying for career opportunities. This interactive initiative would familiarise students with responsible use of AI tools and develop practical skills in application material writing. This could be achieved through three services, namely job description analysis, CV improvement, and mock interview feedback. The student would supply their pre-existing CV, career goals, and the internship or job advert to the model. In return, they would receive an analysis of the advert, suggestions for a compatible CV, and practice questions for a mock interview, if applicable. By synthesising these functions, the tool would urge students to create strong applications to specific roles while pointing out areas needing improvement.

The workshop will embed skills from GitHub (GitHub, n.d.) into a mainstream AI model. An accompanying website could be launched to advertise the AI tool, and fellow societies and departments would be contacted to enhance outreach. Once developed, the prototype would be tested in workshops by university students, and their feedback would be collected to extract insights into functionality and usability. An accompanying website would be launched where research findings and instructions will be displayed. The website would function as an advertising medium for the project and demonstrate the drawbacks and benefits of AI use for navigating career opportunities.

### Conclusion

To conclude, as the abundance of studies in academia suggests, the increasing influence of AI on the job market should be recognised. While this trend exposes university students to some vulnerabilities, these can be mitigated by familiarising them with AI-powered tools when applying for career opportunities. To address this need, our AI literacy project proposes educating an AI-powered tool on how to approach career opportunities alongside interactive workshops. Our project would also encourage students to critically appraise AI-generated content and ensure that their application files align with their skills and experiences. Ultimately, the central objective of our project is to enable students to benefit from technological advancements while preserving their autonomy throughout the job application process.

### References

Abbas Nejad, K., Musillo, G., Wicker, T. and Zaccaria, N. (2025) *Labor Market Signals: The Role of Large Language Models*. https://doi.org/10.2139/ssrn.5185035.

Freeman, J. (2025) *Student Generative AI Survey 2025*. HEPI Policy Note 61. Higher Education Policy Institute. https://www.hepi.ac.uk/reports/student-generative-ai-survey-2025/.

Ganguli, S. (2025). ‘The why and how of generative AI application in business for career readiness’, *International Journal of Advanced Corporate Learning*, 18(1), pp. 64–76. https://doi.org/10.3991/ijac.v18i1.51137.

GitHub (n.d.) *About repositories*. Available at: https://docs.github.com/en/repositories/creating-and-managing-repositories/about-repositories (Accessed: 27 October 2026).

Hou, X. et al. (2024) ‘Large Language Models for Software Engineering: A Systematic Literature Review’, *ACM Transactions on Software Engineering and Methodology*, 33(8), Article 220. https://doi.org/10.1145/3695988.

Shao, M., Basit, A., Karri, R. and Shafique, M. (2024) ‘Survey of Different Large Language Model Architectures: Trends, Benchmarks, and Challenges’, *IEEE Access*, 12, pp. 188664–188706. https://doi.org/10.1109/ACCESS.2024.3482107.

Zhang, S., Dong, L., Li, X., Zhang, S., Sun, X., Wang, S., Li, J., Hu, R., Zhang, T., Wang, G. and Wu, G. (2026) *Instruction Tuning for Large Language Models: A Survey*. *ACM Computing Surveys*. https://doi.org/10.1145/3777411.
"""
    ),
    (
        "Company Profiling",
        """
Company-profiling research serves three chief purposes. It establishes fit in accordance with background, values, mission, people, structure and future plans. This demonstrates whether the company culture is compatible with you. It makes tailoring feasible, since a CV can only be adapted to a firm's language and priorities. It also facilitates the overall process, thereby you prepare for the specific assessment in front of you rather than a generic one.

Employers want someone who adds value, and AI has sharpened rather than softened that. Oxford's careers service reports that applications generated primarily by AI, with little personal input, often appear very similar in content, language and structure, and so fail to communicate a candidate's genuine interests, skills and motivations; hosts consistently find authentic reflection, effort and engagement more compelling (University of Oxford Careers Service, 2025). What hosts want is your experience, your thinking and your way of expressing yourself — so you must say what value you bring beyond being a spare pair of hands.

At this stage, AI is mostly a shortcut to orientation: lists of companies, sector publications and job titles, summaries of public information, explanations of commercial concepts, and broad commentary on strategy. That has a real use. Bright Network recommends generative AI as a creative collaborator for early research, noting that a prompt for trade publications yields a starting point for commercial-awareness work in seconds, and that AI job-matching surfaces roles candidates would not find by scrolling (Bright Network, 2025). Bentley lists matching major, skills and interests to roles as a legitimate use (Walsh, 2025).

The dangers are documented. The most basic is accuracy: these tools present false or outdated information in a confident tone — hallucination (Bright Network, 2025; Walsh, 2025; University of Reading, 2025). Because they cite no evidence, what they do is closer to mashing together content from anywhere in their training data, so source quality cannot be established from the output (University of Reading, 2025). The same property drives duplication: an AI-assisted application may resemble other candidates', which employers read as low effort (Walsh, 2025). Output also drifts towards the generic and cannot identify your particular interest in a company (Walsh, 2025). Nor will it tell you which buzzwords this employer uses, which stances it has taken or what its goals are — precisely what makes an application recognisable as written for one organisation.

Two limits matter if AI is used analytically. Outputs are not neutral: algorithms reproduce the assumptions and biases of their training data, so minority perspectives are underrepresented and over-reliance can block nuanced understanding (University of Reading, 2025). And AI may miss context — including the difference between two things that look very similar but are different (Patron, n.d.). It can help with large amounts of data but cannot replace the creativity, intuition and critical thinking research depends on (ibid.), and the shortcut is not reliably short: iteration involves trial and error, and claims still need independent verification (University of Reading, 2025).

Treat AI as an assistant, not a solution — useful for getting started, initial sector research, a broad structure, or polishing, but never a substitute for well-researched, tailored, personal content (Oxford, 2025). At its most conservative it is safe for refining your own ideas, researching public information and trends, summarising policy proposals, explaining commercial concepts, and serving as a knowledge base you then verify. Bright Network frames it as a starting point rather than a research resource, with AI-generated facts checked against reputable sources (Bright Network, 2025). Oxford advises checking references carefully and testing yourself: if the employer asked whether you had used AI, would you be comfortable explaining how and where (Oxford, 2025)? Rules vary — in Oxford's May 2025 survey only 15% of recruiters allowed or encouraged AI use, while half did not want it — so checking a target's published position is part of the research (ibid.).

The substantive work stays manual, across three strands. First, the organisation's own material: website and social media read alongside news coverage and professional networks to build a picture of market positioning, products, practices and culture — asking what it is known for, its strategy and its core values. Second, its people: research leaders, establish where their remit lies, and consider whether their background connects to yours; LinkedIn is the obvious source. Third, lived experience: hear from employees and interns through blogs, LinkedIn or networking events. Bentley's framing is right to end on — AI is a strong tool for starting the process, but should never be the final product (Walsh, 2025).

## References

- Nathan, D. (2025) *Using generative AI in job applications*, Prospects, June 2025. https://www.prospects.ac.uk/careers-advice/getting-a-job/using-generative-ai-in-job-applications/
- Patron, M. (n.d.) 'Proceed with caution: the potential negative impact of AI on scientific research', *35th MCAA Newsletter*, Marie Curie Alumni Association. https://www.mariecuriealumni.eu/newsletters/35th-mcaa-newsletter/special-issue-proceed-caution-potential-negative-impact-ai-scientific-research
- University of Oxford Careers Service (2025) *Use of AI in job applications and assessments*. https://www.ox.ac.uk/careers/careers-guidance/job-search-and-applications/use-of-ai-in-job-applications-and-assessments
- University of Reading (2025) 'Limitations and risks', *Generative Artificial Intelligence and University Study* (LibGuides). https://libguides.reading.ac.uk/generative-AI-and-university-study/limitations
- Walsh, K. (2025) 'Using AI in your job search: helpful or hurtful?', *Bentley University*, 22 May. https://www.bentley.edu/news/using-ai-your-job-search-helpful-or-hurtful
"""
    ),
    (
        "Cover Letter",
        "Exploring how AI-assisted approaches can help students "
        "develop relevant, tailored and effective cover letters."
    ),
    (
        "CV",
        """
CV (curriculum vitae) is a concise summary of your education, work experience, skills, achievements, and relevant personal details. It is usually the first document. It “is a document that a recruiter should be able to scan quickly and see how your skills and experiences make you the best person for the job,” according to UCL Careers.

It is assessed through initial screening since employers take no more than 7 seconds on your CV, according to UCL Careers. It is reviewed concerning its relevance to the role, evidence of impact, and grammatical clarity. Some employers might also take academic grades, extracurricular endeavours, and transferable skills into account.

AI can be utilised vastly in CV creation. It can generate templates, improve writing, and restructure CVs to a specific job/internship description. However, this process includes many risks. AI can omit nuances, overstate some skills, and produce generic wording. Generic wording can effectively render CVs as superficial as it removes students’ own writing style/voice.

Therefore, students should do the thinking first by creating a compilation of projects, achievement, roles, etc. In this sense, the template provided by UCL Careers would prove useful. Students are advised to scrutinise the criteria of job descriptions and the language of the description. Subsequently, relevant experience should be prioritised and elements should be reordered. At worst, AI might be employed for low-risk uses, such as proofreading and briefly analysing job description demands.
"""
    ),
    (
        "Interview",
        """
### Introduction

Employers typically incorporate interviews into job application processes in order to thoroughly assess whether candidates are suitable for the position applied for. Interviews usually mark the last stage of the application process, and candidates whose application files are deemed to be sufficient could reach such a stage. Interviews supply employers with an opportunity to appraise candidates beyond the information presented in their application documents. This effectively permits them to examine numerous elements such as the candidate’s qualifications, communication skills, and professional experience. Moreover, depending on the recruitment process, interviews may take place at one or several stages. However, how candidates can prepare for interviews may vary depending on the format adopted by employers.

Job interviews can be conducted in many forms, namely structured, semi-structured, and unstructured interviews (Campion, Palmer and Campion, 1997). In structured interviews, all candidates are asked the same set of predetermined questions and a standardised format is followed. Conversely, in semi-structured interviews, additional follow-up questions follow the predetermined questions. Unstructured interviews adopt a rather flexible approach as they do not have predetermined questions. Interviewers are granted freedom to engage in natural discussion.

Employers commonly assess candidates through competency-based, behavioural, and situational questions. These questions aim to establish how candidates have demonstrated relevant skills and competencies in previous experiences and how they might respond to potential workplace situations. The STAR method (Situation, Task, Action, and Result) is frequently employed by candidates to structure their responses to behavioural questions, which enables them to provide clear and relevant examples of their abilities (Bangerter et al., 2023).

### AI Use and Interviews

It is undisputed that most internship or work experience opportunities for university students involve an interview stage. Therefore, students may prefer to use AI tools to prepare for the interview process by generating mock interview questions and possible answers. However, the effectiveness of such preparation may depend on the format of the interview, as different interview types require candidates to demonstrate their abilities in different ways.

AI tools are particularly useful in giving a brief idea of what the candidate should anticipate during this stage. Supporting this, an experiment was conducted on 90 MIT students using an automated conversation coach specifically designed for job interviews. As a result, students who used the system demonstrated improvement in their interview performance (Hoque et al., 2013). Nevertheless, AI tools cannot necessarily predict the behaviour of the interviewer, especially when the interviewer subscribes to a semi-structured or unstructured method. A major risk associated with AI use for interviews is the possibility that answers may be generic and fail to reflect the authentic individual experiences of the candidate (Canagasuriam and Lukacik, 2025). Additionally, AI use might encourage candidates to overly rely on AI-prepared answers. This potentially results in them struggling with unexpected questions or natural discussion. Moreover, it is evident that AI-generated mock interviews would not accurately reproduce the spontaneous nature of real-life interactions. This is because AI-generated mock interviews may not accurately reproduce the spontaneous nature of real-life interactions and hypothetical workplace scenarios.

### Recommendations

Students should approach AI-assisted interview preparation with caution and incorporate their critical thinking into the process. Therefore, AI-generated interviews should be considered solely as an opportunity to practise rather than as a means to craft definitive questions and answers. An effective approach is to educate the AI tool using relevant information. In this context, providing the AI tool with the job description, nature of the interview, and personal CV would facilitate the generation of interview questions specifically compatible with the applied position and personal experience of the candidate, as stated in the CV. Subsequently, students can practise answering these questions without appealing to AI assistance and ask AI tools to provide constructive feedback where needed.

### References

Bangerter et al. (2023) ‘Automatic identification of storytelling responses to past-behavior interview questions via machine learning’, *International Journal of Selection and Assessment*, 31(3), pp. 376–387. https://doi.org/10.1111/ijsa.12428.

Campion, M.A., Palmer, D.K. and Campion, J.E. (1997) ‘A review of structure in the selection interview’, *Personnel Psychology*, 50(3), pp. 655–702. https://doi.org/10.1111/j.1744-6570.1997.tb00709.x.

Canagasuriam, D. and Lukacik, E.-R. (2025) ‘ChatGPT, can you take my job interview? Examining artificial intelligence cheating in the asynchronous video interview’, *International Journal of Selection and Assessment*, 33(1). https://doi.org/10.1111/ijsa.12491.

Hoque, M.E., Courgeon, M., Martin, J.-C., Mutlu, B. and Picard, R.W. (2013) ‘MACH: My Automated Conversation coacH’, *Proceedings of the 2013 ACM International Joint Conference on Pervasive and Ubiquitous Computing*, pp. 697–706. https://doi.org/10.1145/2493432.2493502.
"""
    )
]

for heading, description in sections:
    with st.expander(heading, expanded=False):
        st.markdown(description)


# FOOTER
st.divider()

st.markdown("""
<div style="display:flex;justify-content:flex-end;align-items:flex-end;
color:#777;font-size:13px;padding:8px 0 0 0;">
    <div style="text-align:right;color:#626B77;line-height:1.7;">
        <strong style="color:#182B49;letter-spacing:1px;">CONTACT</strong><br>
        <strong style="color:#182B49;font-size:15px;">Aral Karadayi</strong><br>
        Project Leader<br>
        University College London<br>
        <a href="mailto:aralkaradayi@gmail.com" style="color:#626B77;text-decoration:none;">aralkaradayi@gmail.com</a>
    </div>
</div>
""", unsafe_allow_html=True)
