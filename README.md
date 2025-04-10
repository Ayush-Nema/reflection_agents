Reflection agents
==================

Understanding how to perform Self-reflection in prompting.

--- 

## poetry useful commands
Ref page: [Managing Poetry environments](https://python-poetry.org/docs/managing-environments/#bash-csh-zsh)

### Installation
```commandline
brew install poetry
```

### Create a project and add the dependencies
```commandline
mkdir reflection_agents
cd reflection_agents

poetry init --name reflection-agents --author "Ayush-Nema <contact.ayushnema@gmail.com>" --python ">=3.11,<4.0" --no-interaction

poetry add python-dotenv@">=1.1.0,<2.0.0" \
            langchain@">=0.3.23,<0.4.0" \
            langchain-openai@">=0.3.12,<0.4.0" \
            langgraph@">=0.3.27,<0.4.0"

poetry add --group dev black@">=25.1.0,<26.0.0" isort@">=6.0.1,<7.0.0"
```

### Displaying the environment information
- Basic information: `poetry env info`
- Path of virtual env: `poetry env info --path`
- Path of Python executable: `poetry env info --executable`

#### Listing the environments associated with the project
- List of virtual env associated with current project: `poetry env list`
- Full path of environments: `poetry env list --full-path`

### Delete virtual environment
```commandline
poetry env remove /full/path/to/python
poetry env remove python3.7
poetry env remove 3.7
poetry env remove test-O3eWbxRl-py3.7
```
- Delete all virtual envs all at once (ultimate kill switch!): `poetry env remove --all`
 
### Remove an installed package
```commandline
poetry remove <package-name>
```


![imgs/need_of_LG.png](imgs/need_of_LG.png)  
Point 1-4: General scope of `LangChain`  
Point 5: `LangGraph` supremacy  
Point 6: Full autonomous agent

