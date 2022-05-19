import enum


#TODO naming..
class DeploymentType(enum.Enum):
    LOCAL = 1
    #expose GPUs
    AML_LOCAL = 2
    AML_ON_AKS = 3


MII_CONFIGS_KEY = 'mii_configs'


class Tasks(enum.Enum):
    TEXT_GENERATION = 1
    TEXT_CLASSIFICATION = 2
    QUESTION_ANSWERING = 3
    FILL_MASK = 4
    TOKEN_CLASSIFICATION = 5
    CONVERSATIONAL = 6


TEXT_GENERATION_NAME = 'text-generation'
TEXT_CLASSIFICATION_NAME = 'text-classification'
QUESTION_ANSWERING_NAME = 'question-answering'
FILL_MASK_NAME = 'fill-mask'
TOKEN_CLASSIFICATION_NAME = 'token-classification'
CONVERSATIONAL_NAME = 'conversational'

SUPPORTED_MODEL_TYPES = ['roberta', 'gpt2', 'bert', 'gpt_neo', 'gptj']
SUPPORTED_TASKS = [
    TEXT_GENERATION_NAME,
    TEXT_CLASSIFICATION_NAME,
    QUESTION_ANSWERING_NAME,
    FILL_MASK_NAME,
    TOKEN_CLASSIFICATION_NAME,
    CONVERSATIONAL_NAME
]

MODEL_NAME_KEY = 'model_name'
TASK_NAME_KEY = 'task_name'

ENABLE_DEEPSPEED_KEY = 'ds_optimize'

MII_CACHE_PATH = "MII_CACHE_PATH"
MII_CACHE_PATH_DEFAULT = "/tmp/mii_cache"

MII_DEBUG_MODE = "MII_DEBUG_MODE"
MII_DEBUG_MODE_DEFAULT = "0"

MII_DEBUG_DEPLOY_KEY = "MII_DEBUG_DEPLOY_KEY"

MII_DEBUG_BRANCH = "MII_DEBUG_BRANCH"
MII_DEBUG_BRANCH_DEFAULT = "main"
