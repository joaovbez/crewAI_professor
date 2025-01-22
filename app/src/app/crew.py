from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task
from crewai_tools import SerperDevTool, WebsiteSearchTool
@CrewBase
class CrewProfessorCasd():

	agents_config = 'config/agents.yaml'
	tasks_config = 'config/tasks.yaml'
	@agent
	def teacher(self) -> Agent:
		return Agent(
			config=self.agents_config['Teacher'],
			tools=[
				SerperDevTool(),
				WebsiteSearchTool()
			],
			verbose=True,
			allow_delegation=False
		)
	@agent
	def teacher_cordinator(self) -> Agent:
		return Agent(
			config=self.agents_config['Teacher_Cordinator'],
			verbose=True,
			allow_delegation=False
		)	
	@agent
	def activity_suggester(self) -> Agent:
		return Agent(
			config=self.agents_config['Activity_Suggester'],
			verbose=True,
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
