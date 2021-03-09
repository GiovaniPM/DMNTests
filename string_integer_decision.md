# string_integer_decision

## Dependecies
- [![Python 3.8.1](https://img.shields.io/badge/python-3.9.1-brightgreen.svg)](https://www.python.org/ftp/python/3.9.1/python-3.9.1-amd64.exe)
[![Pip 20.3.3](https://img.shields.io/badge/pip-20.3.3-green.svg)](https://pypi.org/project/pip/)
[![bpmn-dmn 0.1.7](https://img.shields.io/badge/bpmn--dmn-0.1.7-green.svg)](https://pypi.org/project/bpmn-dmn/)
- [![camunda](https://img.shields.io/badge/camunda-4.4.0-brightgreen.svg)](https://camunda.com/download/modeler/)

>## [string_integer_decision.dmn](https://raw.githubusercontent.com/GiovaniPM/DMNTests/main/Rules/string_integer_decision.dmn)
>
>>![string_integer_decision.png](https://raw.githubusercontent.com/GiovaniPM/DMNTests/main/string_integer_decision.PNG)

>## [string_integer_decision.py](https://raw.githubusercontent.com/GiovaniPM/DMNTests/main/string_integer_decision.py)
>
>>``` Python
>>from bpmn_dmn.dmn import DMNDecisionRunner
>>
>>#runner = DMNDecisionRunner('string_integer_decision.dmn', debug='DEBUG')
>>runner = DMNDecisionRunner('./Rules/string_integer_decision.dmn')
>>res = runner.decide('m', 30)
>>print('m,',30,' = ',res.description)
>>res = runner.decide('m', 24)
>>print('m,',24,' = ',res.description)
>>res = runner.decide('m', 45)
>>print('m,',45,' = ',res.description)
>>res = runner.decide('f', 25)
>>print('f,',25,' = ',res.description)
>>res = runner.decide('f', 14)
>>print('f,',14,' = ',res.description)
>>res = runner.decide('f', 45)
>>print('f,',45,' = ',res.description)
>>res = runner.decide('', 0)
>>print(',',0,' = ',res.description)
>>res = runner.decide('x', 8)
>>print('x,',8,' = ',res.description)
>>res = runner.decide('x', 45)
>>print('x,',45,' = ',res.description)
>>```

>## Result
>>``` Python
>>m, 30  =  👨
>>m, 24  =  🙋‍♂️
>>m, 45  =  👴   
>>f, 25  =  👩   
>>f, 14  =  🙋‍♀️
>>f, 45  =  👵   
>>, 0  =  ⁉️     
>>x, 8  =  👶    
>>x, 45  =  ⚠️  
>>```