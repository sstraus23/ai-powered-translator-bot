# AI-Powered Multi-Language Translator Bot

## Project Overview
A serverless, event-driven language translation API that accepts text payloads, dynamically detects languages, executes highly accurate neural translations, and returns audio-ready speech outputs.

## Architecture
* **API Gateway:** Exposes secure REST HTTP endpoints for user payload submission.
* **AWS Lambda:** Processes incoming requests, manages service orchestration, and executes backend logic using Python (Boto3).
* **Amazon Translate:** Performs real-time neural machine translation across targeted language pairs.
* **Amazon Polly:** Synthesizes translated text into natural-sounding speech outputs.

## Technical Stack
* **Cloud Platform:** AWS (API Gateway, Lambda, Amazon Translate, Amazon Polly, IAM, CloudWatch)
* **Languages:** Python (Boto3)

## Engineering Challenges & Debugging Realities
* **The Problem (API Gateway Timeout Management):** During heavy payloads or sequential translation requests, downstream processing occasionally flirted with API Gateway's strict 29-second execution timeout limits.
    * *The Solution:* Optimized execution blocks within the Lambda handler, stripped out redundant payload parsing, and implemented rigorous exception handling to gracefully manage API gateway connection limits without dropping user state.
## System Demo
![Chatbot Conversation Demo](AWS%20LEX%20Github.png)
