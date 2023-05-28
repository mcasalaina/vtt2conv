# vtt2conv
A simple script for converting VTT-formatted transcripts to conversation transcripts supported by Azure Conversation Summarization.

In general, Microsoft Teams emits transcripts in [WebVTT](https://developer.mozilla.org/en-US/docs/Web/API/WebVTT_API) format. However, as of this writing, the [Microsoft Azure Conversation Summarizer](https://learn.microsoft.com/en-us/azure/cognitive-services/language-service/summarization/how-to/conversation-summarization) takes in transcripts in a Name: Words format. This script translates a WebVTT-formatted file into a conversation transcript that Microsoft Azure Conversation Summarizer can handle.

## Usage

**python vtt2conv.py input_filename.vtt [output_filename.vtt]**

If the output filename is not specified, a new file will be created with the same name as the input filename but with a .txt extension.
