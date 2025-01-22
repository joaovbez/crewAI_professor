from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task
from crewai_tools import SerperDevTool, WebsiteSearchTool
from langchain_openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

@CrewBase
class CrewProfessorCasd():

	agents_config = 'config/agents.yaml'
	tasks_config = 'config/tasks.yaml'
	@agent
	def teacher(self) -> Agent:
		return Agent(
			config=self.agents_config['teacher'],
			tools=[
				SerperDevTool(),
				WebsiteSearchTool()
			],
			verbose=True,
			llm="gpt-3.5-turbo-0125",
			allow_delegation=False
		)
	@agent
	def teacher_cordinator(self) -> Agent:
		return Agent(
			config=self.agents_config['teacher_cordinator'],
			verbose=True,
			llm="gpt-3.5-turbo-0125",
			allow_delegation=False
		)	
	@agent
	def activity_suggester(self) -> Agent:
		return Agent(
			config=self.agents_config['activity_suggester'],
			verbose=True,
			llm="gpt-3.5-turbo-0125",
			allow_delegation=False
		)
	@task
	def class_setup(self) -> Task:
		return Task(
			config=self.tasks_config['class_setup'],
		)
	@task
	def class_check(self) -> Task:
		return Task(
			config=self.tasks_config['class_check'],
			output_file='class.md'
		)

	@task
	def class_activities(self) -> Task:
		return Task(
			config=self.tasks_config['class_activities'],			
		)
	
	@crew
	def crew(self) -> Crew:
		return Crew(
			agents=self.agents,
			tasks=self.tasks,
			process=Process.sequential,
			verbose=True,			
		)
