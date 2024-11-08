# @Author: Bertan Berker
# @Language: Python
#
#
#

from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from crewai import Agent, Task, Crew
from crewai_tools import ScrapeWebsiteTool, SerperDevTool
import warnings
warnings.filterwarnings('ignore')
import os
from clarifai_grpc.channel.clarifai_channel import ClarifaiChannel
from clarifai_grpc.grpc.api import service_pb2_grpc
from clarifai_grpc.grpc.api import service_pb2, resources_pb2
from clarifai_grpc.grpc.api.status import status_code_pb2

load_dotenv()
clarifai_api_key = os.getenv('CLARIFAI_API_KEY')
clarifai_application_id = os.getenv('CLARIFAI_APPLICATION_ID')
openai_api_key = os.getenv('OPENAI_API_KEY')
serper_api_key = os.getenv('SERPER_API_KEY')
os.environ["OPENAI_MODEL_NAME"] = 'gpt-3.5-turbo'



def find_videos(topic):
    return

def summarize_video(video_url):

    # TODO Audio-to-speech API for getting the transcript of the video

    summarize_video = Agent(
        role="Video Summarizer Agent",
        goal="Summarize the key learning points of a given youtube video",
        backstory="Specializing in summarizing videos, this ",
        verbose=True,
        allow_delegation=False,
        tools=[SerperDevTool(api_key=serper_api_key)]
    )

    summarize = Task(
        description=(
            "Summarize the key learning points of a given youtube video"
        ),
        expected_output=(
            "A summary of the key learning points of the video in 1-2 sentences and 5-6 bullet points"
        ),
        agent=summarize_video
    )

    video_crew = Crew(
        agents=[summarize_video],
        tasks=[summarize],
        manager_llm=ChatOpenAI(model="gpt-3.5-turbo", temperature=0.7),
        verbose=True
    )

    result = video_crew.kickoff()
    return result


def make_quiz():
    return




