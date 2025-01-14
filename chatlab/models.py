"""Determine which models are available for use in chatlab."""

from enum import Enum


class ChatModel(Enum):
    """Models available for use with chatlab."""

    GPT_4_1106_PREVIEW = "gpt-4-1106-preview"
    GPT_4_VISION_PREVIEW = "gpt-4-vision-preview"

    GPT_4 = "gpt-4"
    GPT_4_0613 = "gpt-4-0613"
    GPT_4_32K = "gpt-4-32k"
    GPT_4_32K_0613 = "gpt-4-32k-0613"
    GPT_3_5_TURBO = "gpt-3.5-turbo"
    GPT_3_5_TURBO_0613 = "gpt-3.5-turbo-0613"
    GPT_3_5_TURBO_16K = "gpt-3.5-turbo-16k"
    GPT_3_5_TURBO_16K_0613 = "gpt-3.5-turbo-16k-0613"


#
# From https://platform.openai.com/docs/guides/gpt/function-calling, the docs say
# that gpt-3.5-turbo-0613 and gpt-4-0613 models support function calling.
# Experimentally, gpt-3.5-turbo-16k also supports function calling.
#
# TODO: Determine if gpt-4-32k supports function calling.
#
class FunctionCompatibleModel(Enum):
    """Models available for use with chatlab."""

    GPT_3_5_TURBO_0613 = "gpt-3.5-turbo-0613"
    GPT_3_5_TURBO_16K_0613 = "gpt-3.5-turbo-16k-0613"
    GPT_4_0613 = "gpt-4-0613"


# Exporting for the convenience of typing e.g. models.GPT_4_0613
GPT_4 = ChatModel.GPT_4.value
GPT_4_0613 = ChatModel.GPT_4_0613.value
GPT_4_32K = ChatModel.GPT_4_32K.value
GPT_4_32K_0613 = ChatModel.GPT_4_32K_0613.value
GPT_3_5_TURBO = ChatModel.GPT_3_5_TURBO.value
GPT_3_5_TURBO_0613 = ChatModel.GPT_3_5_TURBO_0613.value
GPT_3_5_TURBO_16K = ChatModel.GPT_3_5_TURBO_16K.value
GPT_3_5_TURBO_16K_0613 = ChatModel.GPT_3_5_TURBO_16K_0613.value

GPT_4_1106_PREVIEW = ChatModel.GPT_4_1106_PREVIEW.value
GPT_4_VISION_PREVIEW = ChatModel.GPT_4_VISION_PREVIEW.value
