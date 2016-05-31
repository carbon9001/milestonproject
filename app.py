from flask import Flask, render_template, request, redirect, json, url_for
from bokeh.plotting import figure
from bokeh.charts import TimeSeries, vplot
from bokeh.embed import components
import urllib2
import pandas as pd

app = Flask(__name__);

@app.route('/')
def show_index_page():
	return render_template('index.html')
	
# @app.route('/search_and_plot',methods = ['POST'])
# def search_and_plot():
	# error = 'Most likely, the ticker you entered was not found in the dataset.'
	# if request.method == 'POST':
		# ticker = request.form.get('ticker')
		
		# if ( request.form.get('start_year').isdigit() and request.form.get('start_month').isdigit() and request.form.get('start_day').isdigit() ):
			# s_year = str(int(request.form.get('start_year')))
			# s_month = str(int(request.form.get('start_month')))
			# s_day = str(int(request.form.get('start_day')))
		# else:
			# s_year = None
			# s_month = None
			# s_day = None
		
		# if ( request.form.get('end_year').isdigit() and request.form.get('end_month').isdigit() and request.form.get('end_day').isdigit() ):
			# e_year = str(int(request.form.get('end_year')))
			# e_month = str(int(request.form.get('end_month')))
			# e_day = str(int(request.form.get('end_day')))
		# else:
			# e_year = None
			# e_month = None
			# e_day = None
			
		# plotoptions = request.form.getlist('features');
		# #plotoptions = ['Close']
		
		# if(plotoptions):
			# pass
		# else:
			# error = 'please select at least one price item to plot'
			# return render_template('error_page.html', error_message = error)
		
		# if (ticker):
			# require_api_url = "https://www.quandl.com/api/v3/datasets/WIKI/"+ticker+".json?api_key=jn4pYWxH5Q9bn8zTLBUu"
			# #require_api_url = 'https://www.quandl.com/api/v3/datasets/WIKI/FB.json?api_key=jn4pYWxH5Q9bn8zTLBUu'
		# else:
			# return render_template('error_page.html', error_message = error) 
		
		# if(s_year and s_month and s_day):
			# require_api_url += ('&start_date='+s_year+'-'+s_month+'-'+s_day)
		
		# if(e_year and e_month and e_day):
			# require_api_url += ('&end_date='+e_year+'-'+e_month+'-'+e_day)
	
	
	
	# #end of api url generation
	# #start of requesting json
	
	# if require_api_url:
		# try:
			# response = urllib2.urlopen(require_api_url).read()
		# except urllib2.HTTPError, e:
			# return render_template('error_page.html', error_message = error)
		# jsVal = json.loads(response)
		# #for price in jsVal['dataset']['data']:
		# #	return price[0]
		# datafram = pd.DataFrame(jsVal['dataset']['data'],columns = jsVal['dataset']['column_names'])
		# datafram['Date']=pd.to_datetime(datafram['Date'])
		# tsline = TimeSeries(datafram, x='Date', y=plotoptions, color=plotoptions, dash=plotoptions, title="Stock Prices", ylabel='Stock Prices', legend=True)		
		# script, div = components(tsline)
		# stock_fullname = jsVal['dataset']['name']
		# return render_template('plotgraph_page.html',script = script, div = div, stock_fullname = stock_fullname, ticker = ticker)
	# else:
		# return render_template('error_page.html', error_message = error)


if __name__ == '__main__':
	app.run(debug = True)
	