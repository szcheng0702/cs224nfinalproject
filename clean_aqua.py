import re
import json


regex_eq=r'((?<!\n)[\[\(]?([a-z]|((\d*\.)?\d+))([ \)]?[-+/*=\^x]+[ \(]?([a-z]|((\d*\.)?\d+))[\]\)]?)+(?=((\d*\.)?\d+))([a-z]|((\d*\.)?\d+)*)+)'
regex_rm=r'(((\d*\.)?\d+)[ ]?=[ ]?((\d*\.)?\d+))'

#regex_eq=r'(([a-z]|((\d*\.)?\d+))[ ]?[-+/*\^x][ ]?([a-z]|((\d*\.)?\d+))=([a-z]|((\d*\.)?\d+)))'



def read_json_aqua(j_file):
	data = []
	with open(j_file) as f:
		for line in f:
			data.append(json.loads(line))

	q2e={}

	for ex in data:
		if ex.get('question') and ex.get('rationale'):
			
			text=ex['rationale'].replace('\n',' ')
			quest=ex['question'].replace('\n',' ')
			equation_lst=re.findall(regex_eq,text)

			equation=[]

			for eq in equation_lst:

				if eq[0].find('=')!=-1:

					numEnum=re.findall(regex_rm,eq[0])
	
					if numEnum==[]:
						equation.append(eq[0])

			if equation:
				q2e[ex['question']]=' '.join(equation)

	return q2e

def write_json_file(j_file,out_file):
	q2e=read_json_aqua(j_file)

	with open(out_file, 'w') as fp:
		json.dump(q2e, fp)

def generate_source_target_2files(j_file,source_file,target_file):
	q2e=read_json_aqua(j_file)

	with open(source_file, 'w') as f:
		for item in q2e.keys():
			f.write("{}\n".format(item))

	with open(target_file, 'w') as f:
		for item in q2e.values():
			f.write("{}\n".format(item))


generate_source_target_2files('dev.json','AQUARAT_dev_src','AQUARAT_dev_tgt')
write_json_file('dev.json','AQUARAT_dev.json')
#print(q2e)