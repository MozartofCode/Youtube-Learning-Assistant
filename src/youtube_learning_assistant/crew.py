from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task
from crewai_tools import SerperDevTool, YoutubeChannelSearchTool


@CrewBase
class YoutubeLearningAssistantCrew():
	"""YoutubeLearningAssistant crew"""

	@agent
	def channel_researcher(self) -> Agent:
		return Agent(
			config=self.agents_config['channel_researcher'],
			tools=[SerperDevTool],
			verbose=True
		)

	@agent
	def channel_analyzer(self) -> Agent:
		return Agent(
			config=self.agents_config['channel_analyzer'],
			tools=[YoutubeChannelSearchTool],
			verbose=True
		)
	
	@agent
	def quiz_maker(self) -> Agent:
		return Agent(
			config=self.agents_config['quiz_maker'],
			tools=[], #TODO: Add quiz maker tool
			verbose=True
		)
	

	@task
	def research_channel(self) -> Task:
		return Task(
			config=self.tasks_config['research_channel'],
		)

	@task
	def analyze_channel(self) -> Task:
		return Task(
			config=self.tasks_config['analyze_channel'],
		)


	@task
	def create_quiz(self) -> Task:
		return Task(
			config=self.tasks_config['create_quiz'],
			#output_file='report.md'
		)
	

	@crew
	def crew(self) -> Crew:
		"""Creates the YoutubeLearningAssistant crew"""
		return Crew(
			agents=self.agents,
			tasks=self.tasks,
			process=Process.sequential,
			verbose=True,
		)