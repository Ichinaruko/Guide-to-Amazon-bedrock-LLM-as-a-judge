### Guide-to-Amazon-bedrock-LLM-as-a-judge

Amazon Bedrock allows developers to build and deploy AI applications using foundation models (FMs) from multiple providers. Using a Large Language Model (LLM) as a judge in Amazon Bedrock means leveraging LLMs to evaluate, rank, or provide feedback on various inputs, such as text generation, sentiment analysis, or even decision-making tasks.

Amazon Bedrock allows developers to build and deploy AI applications using foundation models (FMs) from multiple providers. Using a **Large Language Model (LLM) as a judge** in Amazon Bedrock means leveraging LLMs to evaluate, rank, or provide feedback on various inputs, such as text generation, sentiment analysis, or even decision-making tasks.

### **How an LLM Acts as a Judge in Amazon Bedrock**
1. **Evaluating AI-generated Content**  
   - The LLM can assess AI-generated responses for correctness, coherence, and relevance.  
   - Example: Checking chatbot responses for accuracy in customer support.

2. **Ranking and Scoring Responses**  
   - The model can assign scores based on predefined criteria.  
   - Example: Ranking product descriptions based on clarity and persuasiveness.

3. **Providing Justifications and Explanations**  
   - LLMs can explain why a particular response is better than another.  
   - Example: In legal or ethical AI applications, justifying why an answer aligns with policies.

4. **Automated Decision-Making**  
   - Can be used in workflows where AI needs to validate input and determine the best course of action.  
   - Example: Filtering inappropriate content in a moderation system.

### **Implementation in Amazon Bedrock**
- **Choose an LLM**  
  Amazon Bedrock provides access to various foundation models from **Anthropic (Claude), AI21 Labs (Jurassic), Meta (Llama), Cohere**, and others.  
- **Define Evaluation Criteria**  
  Define what makes a "good" response—accuracy, clarity, ethical alignment, etc.  
- **Prompt Engineering**  
  Craft detailed prompts for the LLM to provide structured judgments.  
- **Automation & Integration**  
  Use **AWS Lambda** and **Bedrock API** to automate evaluations in workflows.

## **Prerequisites**

### **LLM-as-a-Judge Model Evaluation Prerequisites**  

 **AWS Account & Model Access**  
- Ensure you have an **active AWS account**.  
- Enable **evaluator and generator models** in **Amazon Bedrock**.  
- Verify model access on the **Model Access page** in the Bedrock console.  
- Check **AWS regions** where the model is available and confirm your **quotas**.  

 **IAM & S3 Bucket Setup**  
- Complete **AWS Identity and Access Management (IAM) setup**.  
- Add necessary **IAM permissions** for your S3 bucket to **read and write output data**.  
- Enable **CORS (Cross-Origin Resource Sharing) on your S3 bucket**.  

 **Custom Model Considerations (If Applicable)**  
- If using a **custom model**, ensure **sufficient quota** for **Provisioned Throughput** during inference.  
- Complete the prerequisites for **importing a custom model**.  

 **Check AWS Service Quotas**  
- Go to **AWS Service Quotas Console** and check:  
  - **Model units no-commitment Provisioned Throughputs** across custom models.  
  - **Model units per provisioned model** for your specific custom model.  
- If needed, **request a quota increase** to accommodate your workload.  

# **PREPARING A DATASET**

Prepare input dataset
When preparing your dataset for LLM-as-a-judge model evaluation jobs, each prompt must include specific key-value pairs. Here are the required and optional fields:

- prompt (required): This key indicates the input for various tasks. It can be used for general text generation where the model needs to provide a response, question-answering tasks where the model must answer a specific question, text summarization tasks where the model needs to summarize a given text, or classification tasks where the model must categorize the provided text.

- referenceResponse (used for specific metrics with ground truth): This key contains the ground truth or correct response. It serves as the reference point against which the model’s responses will be evaluated if it is provided.

- category (optional): This key is used to generate evaluation scores reported by category, helping organize and segment evaluation results for better analysis.

DATASET REQUIREMENTS --

- Each line must be a valid JSON object
  
- The file must use JSONL format
  
- The dataset should be stored in an Amazon S3 bucket

example of a proper JSONL file that you can use :
```
#{"prompt": "Can you explain the theory of relativity in simple terms?", "category": "Readability", "referenceResponse": "The theory of relativity, developed by Einstein, explains how space and time are linked. It says that time moves slower when you're moving very fast and that gravity can bend space-time."}
#{"prompt": "How can I improve my time management skills?", "category": "Helpfulness", "referenceResponse": "You can improve time management by setting clear goals, prioritizing tasks, avoiding distractions, and using time-blocking techniques."}
#{"prompt": "Write a well-structured summary of the book 'To Kill a Mockingbird'.", "category": "Coherence", "referenceResponse": "Harper Lee's 'To Kill a Mockingbird' is a novel set in the American South during the 1930s. It follows Scout Finch as she navigates issues of racism, justice, and morality in her small town."}
```

### MAKING AN S3 BUCKET 

1. Go to you Amazon Bedrock, search up S3 Bucket and go to said option.

2. Click on Create Bucket.
   ![image](https://github.com/user-attachments/assets/b2ee3ce4-0210-4acd-acc7-c7a8d4b17c4c)

3. Give your Bucket a name and then save the bucket 
   ![image](https://github.com/user-attachments/assets/4774dd4d-e5a1-422d-af31-9e549d1e3dd9)

4. Once your bucket is done, you are good to drag and drop your files into it.
   ![image](https://github.com/user-attachments/assets/d142ce5d-75f4-4a0e-a9c8-50def8eb2ad9)

5. Now to set up the CORS permissions, go to permissions tab in your S3 Bucket you just made.
   ![image](https://github.com/user-attachments/assets/c4f31b10-f4ad-4f89-82af-280bc0ba1030)

6. Click on Edit on the CORS tab
   ![image](https://github.com/user-attachments/assets/2d1fad82-46bf-45f1-b3be-9dd097d0384c)

7. ```
   [
    {
        "AllowedHeaders": [
            "*"
        ],
        "AllowedMethods": [
            "GET",
            "PUT",
            "POST",
            "DELETE"
        ],
        "AllowedOrigins": [
            "*"
        ],
        "ExposeHeaders": [
            "Access-Control-Allow-Origin"
        ]
    }
   ]
   ```
   PASTE THIS THERE

### Start an LLM-as-a-judge model evaluation job using the console 

You can use LLM-as-a-judge on Amazon Bedrock Model Evaluation to assess model performance through a user-friendly console interface. Follow these steps to start an evaluation job:

1. In the Amazon Bedrock console, choose Inference and Assessment and then select Evalutaions. On the Evaluations page, choose the Models
   ![image](https://github.com/user-attachments/assets/54d2af99-cdc8-4106-9241-1a086b5341b9)

2. Choose **Create** and select Automatic: LLM-as-a-judge.

3. Enter a name and description and select an Evaluator model. This model will be used as a judge to evaluate the response of a prompt or model from your generative AI application.
   ![image](https://github.com/user-attachments/assets/52e723bc-0c86-4a05-9997-b34f111896fa)

4. Choose Tags(Optional) and select the model to be used for generating responses in this evaluation job.
   ![image](https://github.com/user-attachments/assets/f85f13aa-875a-4e8a-88c6-912063279f3e)

5. Select the metrics you want to use to evaluate the model response (such as helpfulness, correctness, faithfulness, relevance, and harmfulness).
   ![image](https://github.com/user-attachments/assets/e9774c55-130f-4243-8b51-ded29fa1ac0e)

6. Select the S3 URI for Choose a prompt dataset and for Evaluation results. You can use the Browse S3 option.
   ![image](https://github.com/user-attachments/assets/0b3cb49b-27e3-4038-bd54-371285f3a0d0)

7. Select or create an IAM service role with the proper permissions. This includes service access to Amazon Bedrock, the S3 buckets in the evaluation job, and the models being used in 
   the job. If you create a new IAM role in the evaluation setup, the service will automatically give the role the proper permissions for the job. Specify the output S3 bucket and 
   choose Create.
   ![image](https://github.com/user-attachments/assets/5d347adb-a789-49e1-a888-ca17f93031f3)

8. You will be able to see the evaluation job is In Progress. Wait for the job status to change to Complete.
   ![image](https://github.com/user-attachments/assets/0edb1d79-621a-4935-a2e3-bf491ada5e97)

9. When complete, select the job to see its details. The following is the metrics summary (such as 0.83 for helpfulness, 1.00 for correctness, 1.00 for faithfulness, 1.00 for relevance, 
   and 0.00 for harmfulness etc etc...
   ![image](https://github.com/user-attachments/assets/93000d52-303a-455c-a0d8-36dbe02310ce)

10. To view generation metrics details, scroll down in the model evaluation report and choose any individual metric (like helpfulness or correctness)
    ![image](https://github.com/user-attachments/assets/f51d0eae-36c4-4aa7-9fb1-43aed69b854f)

11. To see each record’s prompt input, generation output, ground truth, and individual scores, choose a metric and select “Prompt details”. Hover over any individual score to view its 
    detailed explanation.
    ![image](https://github.com/user-attachments/assets/c3767bd9-6a4c-4c92-8f0e-50adbb9a4f72)




