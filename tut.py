from flask import Flask, render_template, request
import pandas as pd


app = Flask(__name__)

@app.route('/')
def index():
	return render_template('index.html')

@app.route('/nf/')                                       #nf = Noun Inflextion
def nf():
	return render_template('nf.html')

@app.route('/ns/')
def ns():
	return render_template('ns.html')

@app.route('/pf/')
def pf():
	return render_template('pf.html')

@app.route('/ps/')
def ps():
	return render_template('ps.html')

@app.route('/vf/')
def vf():
	return render_template('vf.html')

@app.route('/vs/')
def vs():
	return render_template('vs.html')

@app.route('/n_f')
def n_f():
	return render_template('noun1.html')

@app.route('/p_f')
def p_f():
	return render_template('pronoun.html')

@app.route('/v_f')
def v_f():
	return render_template('verb1.html')


@app.route('/nf1', methods=['POST'])
def nf1():
	wo = request.form['word']
	df = pd.read_excel (r'noun_rules.xlsx') 
	df2=pd.read_csv(r"lexicon.csv")
	X = df2.iloc[:, 0].values
	Y = df2.iloc[:, 3].values
	x=list(X)
	y=list(Y)
	
	if wo in x:
		z = x.index(wo)
		category=y[z]#Change here when sql database is available
		o = category
		o = int(o)
		#####Got the word,category
		df.reset_index(inplace=True)
		p=df.loc[ o-1 , : ]
		p=list(p)
		p.pop(0)
		p.pop(0)
		p.pop(0)
		


		inflex_morh=list()
		for i in p:
		    new_word=wo+i
		    inflex_morh.append(new_word)
		    
		n=inflex_morh
		#return n[13]
		#print (df)
		return render_template('npf.html',in1=n[0],in2=n[1],in3=n[2],in4=n[3],in5=n[4],in6=n[5],in7=n[6],in8=n[7],in9=n[8],in10=n[9],in11=n[10],in12=n[11],in13=n[12],in14=n[13])
	else:
		return render_template('back.html')

@app.route('/ns1', methods=['POST'])
def ns1():
	wo = request.form['word']
	df = pd.read_excel (r'noun_rules.xlsx') 
	df2=pd.read_csv(r"lexicon.csv")
	X = df2.iloc[:, 0].values
	Y = df2.iloc[:, 3].values
	x=list(X)
	y=list(Y)
	if wo in x:
		z = x.index(wo)
		category=y[z]                                  #Change here when sql database is available
		o = category
		o = int(o)
		#####Got the word,category
		df.reset_index(inplace=True)
		p=df.loc[ o-1 , : ]
		p=list(p)
		p.pop(0)
		p.pop(0)
		p.pop(0)
		


		inflex_morh=list()
		for i in p:
		    new_word=wo+i
		    inflex_morh.append(new_word)
		    
		n=inflex_morh

		specific=["P1","P2","P3","P4","P5","P6","P7","P8","P9","P10","P11","P12","P13","P14"]
		cat = request.form['ca']
		index=specific.index(cat)
		return render_template('nps.html',w=wo,c=cat,sp=inflex_morh[index])
	else:
		return render_template('back.html')
	    

@app.route('/pf1', methods=['POST'])
def pf1():
	wo = request.form['word']
	dataset = pd.read_excel(r'pn.xlsx')

	X = dataset.iloc[:, 2].values
	Y = dataset.iloc[:, 2:16].values

	x=list(X)
	if wo in x:
		pos=x.index(wo)
		n=Y[pos]
		return render_template('npf.html',in1=n[0],in2=n[1],in3=n[2],in4=n[3],in5=n[4],in6=n[5],in7=n[6],in8=n[7],in9=n[8],in10=n[9],in11=n[10],in12=n[11],in13=n[12],in14=n[13])
	else:
		return render_template('back.html')

@app.route('/ps1', methods=['POST'])
def ps1():
	wo = request.form['word']
	dataset = pd.read_excel(r'pn.xlsx')

	X = dataset.iloc[:, 2].values
	Y = dataset.iloc[:, 2:16].values

	x=list(X)
	if wo in x:
		pos=x.index(wo)
		n=Y[pos]
		specific=["P1","P2","P3","P4","P5","P6","P7","P8","P9","P10","P11","P12","P13","P14"]
		cat = request.form['ca']
		index=specific.index(cat)
		return render_template('nps.html',w=wo,c=cat,sp=n[index])
	else:
		return render_template('back.html')


@app.route('/vf1', methods=['POST'])
def vf1():
	wo = request.form['word']
	df_verb = pd.read_excel (r'verb.xlsx')
	df2=pd.read_csv(r"lexicon.csv")
	X = df2.iloc[:, 0].values
	Y = df2.iloc[:, 3].values
	Y1 = df2.iloc[:, 4].values
	Y2 = df2.iloc[:, 5].values
	x=list(X)
	y=list(Y)
	y1=list(Y1)
	y2=list(Y2)
	if wo in x:
		z = x.index(wo)
		r=y[z]
		m = ['1R','2R','1F','2F','1S','2S','3S','4S','5S','6S','7S','8S','9S','10S']
		o=m.index(r)
		row=df_verb.loc[o , :]
		row=list(row)
		row.pop(0)
		row.pop(0)
		inflex_morh_verb=list()
		for i in row:
		    new_word=wo+i
		    inflex_morh_verb.append(new_word)
		n=inflex_morh_verb
		
		f=y1[z]
		o1 = m.index(f)
		row_f=df_verb.loc[o1 , :]
		row_f=list(row_f)
		row_f.pop(0)
		row_f.pop(0)

		inflex_morh_verb_f=list()
		for i in row_f:
		    new_word=wo+i
		    inflex_morh_verb_f.append(new_word)
		    
		a1 = inflex_morh_verb_f

		s=y2[z]
		o2 = m.index(s)
		row_s=df_verb.loc[o2 , :]
		row_s=list(row_s)
		row_s.pop(0)
		row_s.pop(0)

		inflex_morh_verb_s=list()
		for i in row_s:
		    new_word=wo+i
		    inflex_morh_verb_s.append(new_word)
		    
		b1 = inflex_morh_verb_s
		#return n[9]
		return render_template('ivf.html',a=n[0],aa=n[1],aas=n[2],ad=n[3],af=n[4],ag=n[5],ah=n[6],aj=n[7],ak=n[8],al=n[9],q=a1[0],qw=a1[1],qe=a1[2],qr=a1[3],qt=a1[4],qy=a1[5],qu=a1[6],qi=a1[7],qo=a1[8],qp=a1[9],z=b1[0],zz=b1[1],x=b1[2],xx=b1[3],c=b1[4],cc=b1[5],v=b1[6],vv=b1[7],b=b1[8],bb=b1[9])
	else:
		return render_template('back.html')


@app.route('/vs1', methods=['POST'])
def vs1():
	wo = request.form['word']
	df_verb = pd.read_excel (r'verb.xlsx')
	df2=pd.read_csv(r"lexicon.csv")
	X = df2.iloc[:, 0].values
	Y = df2.iloc[:, 3].values
	Y1 = df2.iloc[:, 4].values
	Y2 = df2.iloc[:, 5].values
	x=list(X)
	y=list(Y)
	y1=list(Y1)
	y2=list(Y2)
	if wo in x:
		z = x.index(wo)
		r=y[z]
		m = ['1R','2R','1F','2F','1S','2S','3S','4S','5S','6S','7S','8S','9S','10S']
		o=m.index(r)
		row=df_verb.loc[o , :]
		row=list(row)
		row.pop(0)
		row.pop(0)
		inflex_morh_verb=list()
		for i in row:
		    new_word=wo+i
		    inflex_morh_verb.append(new_word)
		n=inflex_morh_verb
		
		f=y1[z]
		o1 = m.index(f)
		row_f=df_verb.loc[o1 , :]
		row_f=list(row_f)
		row_f.pop(0)
		row_f.pop(0)

		inflex_morh_verb_f=list()
	
		for i in row_f:
		    new_word=wo+i
		    inflex_morh_verb_f.append(new_word)
		    
		a1 = inflex_morh_verb_f

		s=y2[z]
		o2 = m.index(s)
		row_s=df_verb.loc[o2 , :]
		row_s=list(row_s)
		row_s.pop(0)
		row_s.pop(0)

		inflex_morh_verb_s=list()
		print("S Series")
		for i in row_s:
		    new_word=wo+i
		    inflex_morh_verb_s.append(new_word)
		    
		b1 = inflex_morh_verb_s
		cat=request.form['ca']#P1,p2...
		tense=request.form['te']#S,f,p
		specific=["P1","P2","P3","P4","P5","P6","P7","P8","P9","P10"]
		indexx=specific.index(cat)

		if tense=="R":
		    return render_template('svf.html',w=wo,c=cat,t=tense,sp=inflex_morh_verb[indexx])
		    

		elif tense=="F":
		    return render_template('svf.html',w=wo,c=cat,t=tense,sp=inflex_morh_verb_f[indexx])
		    
		elif tense=="S":
		    return render_template('svf.html',w=wo,c=cat,t=tense,sp=inflex_morh_verb_s[indexx])
	else:
		return render_template('back.html')

if __name__ == '__main__':
	app.run(debug = True)