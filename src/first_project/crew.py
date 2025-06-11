from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task
from crewai.agents.agent_builder.base_agent import BaseAgent
from typing import List
# If you want to run a snippet of code before or after the crew starts,
# you can use the @before_kickoff and @after_kickoff decorators
# https://docs.crewai.com/concepts/crews#example-crew-class-with-decorators

@CrewBase
class FirstProject():
    """FirstProject crew"""

    agents: List[BaseAgent]
    tasks: List[Task]

    # Learn more about YAML configuration files here:
    # Agents: https://docs.crewai.com/concepts/agents#yaml-configuration-recommended
    # Tasks: https://docs.crewai.com/concepts/tasks#yaml-configuration-recommended
    
    # If you would like to add tools to your agents, you can learn more about it here:
    # https://docs.crewai.com/concepts/agents#agent-tools
    @agent
    def executive_assistant(self) -> Agent:
        return Agent(
            config=self.agents_config['executive_assistant'], # type: ignore[index]
            verbose=True,
            allow_delegation=True
        )

    @agent
    def researcher(self) -> Agent:
        return Agent(
            config=self.agents_config['researcher'], # type: ignore[index]
            verbose=True,
            allow_delegation=False
        )
    
    @agent
    def reporting_analyst(self) -> Agent:
        return Agent(
            config=self.agents_config['reporting_analyst'], # type: ignore[index]
            verbose=True,
            allow_delegation=False
        )

    @agent
    def excel_specialist(self) -> Agent:
        return Agent(
            config=self.agents_config['excel_specialist'], # type: ignore[index]
            verbose=True,
            allow_delegation=False
        )

    @agent
    def ppt_creator(self) -> Agent:
        return Agent(
            config=self.agents_config['ppt_creator'], # type: ignore[index]
            verbose=True,
            allow_delegation=False
        )

    @agent
    def qa_reviewer(self) -> Agent:
        return Agent(
            config=self.agents_config['qa_reviewer'], # type: ignore[index]
            verbose=True,
            allow_delegation=False
        )

    @agent
    def scheduler(self) -> Agent:
        return Agent(
            config=self.agents_config['scheduler'], # type: ignore[index]
            verbose=True,
            allow_delegation=True
        )

    @agent
    def communication_assistant(self) -> Agent:
        return Agent(
            config=self.agents_config['communication_assistant'], # type: ignore[index]
            verbose=True,
            allow_delegation=True
        )

    # To learn more about structured task outputs,
    # task dependencies, and task callbacks, check out the documentation:
    # https://docs.crewai.com/concepts/tasks#overview-of-a-task
    @task
    def executive_task(self) -> Task:
        return Task(
            config=self.tasks_config['executive_task'], # type: ignore[index]
            output_file='executive_report.md',
            language="ja",
        )

    @task
    def research_task(self) -> Task:
        return Task(
            config=self.tasks_config['research_task'], # type: ignore[index]
            output_file='research_report.md',
            language="ja",
            context=[
                self.executive_task()
            ]
        )

    @task
    def reporting_task(self) -> Task:
        return Task(
            config=self.tasks_config['reporting_task'], # type: ignore[index]
            output_file='report.md',
            language="ja"
        )


    @task
    def excel_task(self) -> Task:
        return Task(
            config=self.tasks_config['excel_task'], # type: ignore[index]
            output_file='excel_analysis.xlsx',
            language="ja"
        )

    @task
    def ppt_task(self) -> Task:
        return Task(
            config=self.tasks_config['ppt_task'], # type: ignore[index]
            output_file='presentation.pptx',
            language="ja"
        )

    @task
    def qa_task(self) -> Task:
        return Task(
            config=self.tasks_config['qa_task'], # type: ignore[index]
            output_file='qa_review.md',
            language="ja"
        )

    @task
    def schedule_task(self) -> Task:
        return Task(
            config=self.tasks_config['schedule_task'], # type: ignore[index]
            output_file='schedule_report.md',
            language="ja"
        )

    @task
    def communication_task(self) -> Task:
        return Task(
            config=self.tasks_config['communication_task'], # type: ignore[index]
            output_file='communication_log.md',
            language="ja"
        )

    @crew
    def crew(self) -> Crew:
        """Creates the FirstProject crew"""
        # To learn how to add knowledge sources to your crew, check out the documentation:
        # https://docs.crewai.com/concepts/knowledge#what-is-knowledge

        return Crew(
            agents=self.agents, # Automatically created by the @agent decorator
            tasks=self.tasks, # Automatically created by the @task decorator
            process=Process.sequential,
            verbose=True,
            language="ja", 
            # process=Process.hierarchical, # In case you wanna use that instead https://docs.crewai.com/how-to/Hierarchical/
        )
