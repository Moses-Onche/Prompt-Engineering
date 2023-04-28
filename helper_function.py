#!/usr/bin/python3
"""Helper funciton to make it easier to see generated outputs."""
import openai


def get_completion(prompt, model='gpt-3.5-turbo'):
    messages = [{'role': 'user', 'content': prompt}]
    response = openai.ChatCompletion.create(
            model=model,
            messages=messages,
            #   This is the degree of randomness of the model's output
            temperature=0
    )
    return response.choices[0].message['content']
