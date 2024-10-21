from ..base import BaseModel
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.messages import SystemMessage
from langchain_core.documents import Document


class ChatGPT(BaseModel):
    def __init__(self):
        super().__init__(config={"model": ChatOpenAI(model="gpt-4o-mini"), "parser": StrOutputParser()})
        self.prompt_template = ChatPromptTemplate.from_messages(
            [
                SystemMessage(content="say hello"),
            ]
        )

    def set_prompt_template(self):
        system_prompt = (
            "system",
            """You are an extremely selective and critical automated resume review system for {company}.  You will receive a job description for a position that {company} is hiring for along with a resume and cover letter for somebody applying to that role.  Your job is to asses whether or not the applicant should be considered for the role described in the job description.  Your output should contain an answer between one and ten on how good the applicant is for the job.  Your output should also include recommendations for how the candidate could improve their resume and cover letter to better fit the job description.  Please list your recommendations in bulleted form and keep the suggestions direct and to the point.""",
        )
        user_prompt = (
            "user",
            """Job Description: {job_description_text}
            Resume: {resume}
            Cover Letter:{cover_letter} """,
        )
        self.prompt_template = ChatPromptTemplate.from_messages([system_prompt, user_prompt])

    def call_model(self, company: str, job_description_text: str, resume: Document, cover_letter: Document):
        self.set_prompt_template()
        chain = self.prompt_template | self.model | self.parser
        return chain.invoke(
            {
                "company": company,
                "job_description_text": job_description_text,
                "resume": resume,
                "cover_letter": cover_letter,
            }
        )
