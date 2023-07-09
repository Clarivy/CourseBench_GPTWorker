# CourseBench Feedback Refinement System

This project is a FastAPI application that uses a GPT generator to refine the language used in forum messages. The system filters out inappropriate words or phrases, ensuring a positive and constructive environment for university students to discuss and comment on their courses.

The refinement is following code below in ``example/system.txt``

* Leaving well-structured and informative messages unaltered
* Preserving main points of critical and emotive messages while removing offensive language
* Transforming highly emotional messages into more objective ones
* Restructuring incoherent or disorganized messages to improve clarity
* If encountering unfamiliar words or phrases, feel free to disregard them
* For messages containing sarcastic or mocking, maintain the original content as long as it does not include insults directed at a professor's character
* Negative comments about courses or teaching methods are permissible, but refrain from using offensive words regarding a professor's personality.

## Features

- Exposes a POST endpoint at /v1/generate which accepts parameters for content and title.
- Uses a GPT generator to generate responses based on the provided content and title.
- Handles exceptions during the generation of messages, returning a HTTPException with status code 500.

## Installation

The project requires Python 3.10.12 and the dependencies listed in the `requirements.txt` file. You can install these dependencies using pip:

```bash
pip install -r requirements.txt
```

## Usage

To start the server, run the following command:

```bash
uvicorn app:app --port 80 --host 0.0.0.0
```

To use the /v1/generate endpoint, send a POST request with a JSON body containing the title and content parameters. For example:

```json
{
  "title": "Course Feedback",
  "content": "The course was challenging but rewarding."
}
```

## Docker

A Dockerfile is provided for containerization. To build and run the Docker container, use the following commands:

```bash
docker build -t course-feedback-refinement-system .
docker run -p 80:80 course-feedback-refinement-system
```

## Testing

Test cases are provided in the testcases directory. Each test case is a markdown file containing a message that needs to be refined.

## Contributing

Contributions are welcome. Please make sure to update the test cases as appropriate when making a change.

## License

This project is licensed under the terms of the MIT license.

## Acknowledge

Documentation is written with GPT-4.