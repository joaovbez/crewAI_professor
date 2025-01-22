#!/usr/bin/env python
import sys
import warnings

from src.app.crew import CrewProfessorCasd

warnings.filterwarnings("ignore", category=SyntaxWarning, module="pysbd")

def run(inputs):    
    return CrewProfessorCasd().crew().kickoff(inputs=inputs, return_all_outputs=True)


if __name__ == "__main__":
    run()