#!/usr/bin/env python
import sys
import warnings

from app.crew import CrewProfessorCasd

warnings.filterwarnings("ignore", category=SyntaxWarning, module="pysbd")

def run():
    inputs = {
        'main topic': 'similarity of triangles'
    }
    CrewProfessorCasd().crew().kickoff(inputs=inputs)


if __name__ == "__main__":
    run()