# Heron Coding Challenge - File Classifier

## Initial Thoughts - Limitations
- **very** user dependent as assumes users utilise consistent naming conventions for files and also name files correctly (i.e bank_statement_1 is actually a bank statement)
- no centralised list of classifications (hard coded in if statement, not scalable and difficult to maintain - valid file types also difficult to maintain)
- no testing of classification function
- no Dockerfile for easy deployment

## Approach
Given time constraints of the challenge, focused on removing user dependency in classification process as felt like this was the highest priority / would deliver the biggest improvement in terms of accuracy (i.e hopefully fewer unknowns / incorrectly labelled files for the automations):

1. researched conversion of files into text: unfortunately no one-size-fits-all approach here, so focused on allowed extensions as given current industries, likely covers a good % of documents processed (PDF, JPEG & PNG)
2. decided on pypdf for pdf and pytesseract for image conversion - built logic into classifier function and tested returned text using example files saved in project folder
3. created Open AI chat completion input message (using text examples as a guide for LLM) and used text generated by pypdf / pytesseract for classification prompt (disclaimer: took a very hacky few-shot learning approach here!)
4. tested API calls using the example files and iterated the prompt until desired output / output format was returned
5. researched tests for pypdf, pytesseract and openai

**Note:** made decision not to include file name as a first step in the classification process as in my experience, files sent from vendors usually have obscure names plus I don't think file name validation would be an amazing UX, especially at higher volumes (could be wrong here!). However, do recognise that it would remove the need to send an API call with every document, so may be something to consider ...

## Improvements / Next Steps:
- write tests to cover classifier functionality (relevant github repos commented as placeholders in file)
- improve Open AI prompt i.e how can I add more classifications in a scalable way
- add logic to convert additional file types to text (as ideally want the classifier to work across as many file types as possible
- look into extracting classifications / valid file types into a database as a central source of truth across all related applications
- utilitise python-magic library to determine file type for more accurate validation (from a quick search, seemed like this was the best option)
- refactor codebase using SOLID principles
- add a Dockerfile and set up a CI/CD pipeline for automated deployment

## Instructions:
1. Clone the repository:
    ```shell
    git clone <repository_url>
    cd heron_classifier
    ```

2. Install dependencies:
    ```shell
    python -m venv venv
    source venv/bin/activate
    pip install -r requirements.txt
    ```
    
3. Install Google Tesseract OCR (https://github.com/tesseract-ocr/tesseract)
   ```
   brew install tesseract
   ```
   
5. Create an Open AI account & create a new API key
   ```
   https://platform.openai.com/docs/overview
   ```
   
6. Create a .env file & add the below environment variables
   ```shell
   TESSERACT_EXE=/path/to/tesseract/exe
   OPENAI_API_KEY=insert_your api_key_here
   ```

7. Run the Flask app:
    ```shell
    python -m src.app
    ```

4. Test the classifier using a tool like curl:
    ```shell
    curl -X POST -F 'file=@path_to_pdf.pdf' http://127.0.0.1:5000/classify_file
    ```

5. Run tests:
   ```shell
    pytest
    ```
<br>

# Challenge Details

## Overview

At Heron, we’re using AI to automate document processing workflows in financial services and beyond. Each day, we handle over 100,000 documents that need to be quickly identified and categorised before we can kick off the automations.

This repository provides a basic endpoint for classifying files by their filenames. However, the current classifier has limitations when it comes to handling poorly named files, processing larger volumes, and adapting to new industries effectively.

**Your task**: improve this classifier by adding features and optimisations to handle (1) poorly named files, (2) scaling to new industries, and (3) processing larger volumes of documents.

This is a real-world challenge that allows you to demonstrate your approach to building innovative and scalable AI solutions. We’re excited to see what you come up with! Feel free to take it in any direction you like, but we suggest:


### Part 1: Enhancing the Classifier

- What are the limitations in the current classifier that's stopping it from scaling?
- How might you extend the classifier with additional technologies, capabilities, or features?


### Part 2: Productionising the Classifier 

- How can you ensure the classifier is robust and reliable in a production environment?
- How can you deploy the classifier to make it accessible to other services and users?

We encourage you to be creative! Feel free to use any libraries, tools, services, models or frameworks of your choice

### Possible Ideas / Suggestions
- Train a classifier to categorize files based on the text content of a file
- Generate synthetic data to train the classifier on documents from different industries
- Detect file type and handle other file formats (e.g., Word, Excel)
- Set up a CI/CD pipeline for automatic testing and deployment
- Refactor the codebase to make it more maintainable and scalable

## Marking Criteria
- **Functionality**: Does the classifier work as expected?
- **Scalability**: Can the classifier scale to new industries and higher volumes?
- **Maintainability**: Is the codebase well-structured and easy to maintain?
- **Creativity**: Are there any innovative or creative solutions to the problem?
- **Testing**: Are there tests to validate the service's functionality?
- **Deployment**: Is the classifier ready for deployment in a production environment?

## Submission

Please aim to spend 3 hours on this challenge.

Once completed, submit your solution by sharing a link to your forked repository. Please also provide a brief write-up of your ideas, approach, and any instructions needed to run your solution. 
