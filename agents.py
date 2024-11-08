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
    return

def make_quiz():
    return




