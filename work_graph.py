import plotly
import plotly.plotly as pl
import plotly.figure_factory as ff
import datetime
plotly.tools.set_credentials_file(username='bleakair', api_key='nYDHEuzVBFmkX2JNKCv9')

present = datetime.datetime.today().strftime('%Y-%m-%d')

df = [dict(Task="Freedom IHE", Start='2015-11-15', Finish='2017-02-15', Resource='Web Dev'),
      dict(Task="HCC Intern", Start='2016-11-15', Finish='2016-12-28', Resource='Data Analysis'),
      dict(Task="Spark", Start='2016-04-15', Finish='2017-07-15', Resource='Technician'),
      dict(Task="Wintec (Work)", Start='2018-08-15', Finish=present, Resource='Peer tutor'),
      dict(Task="Wintec (Study)", Start='2016-07-15', Finish='2016-11-15', Resource='Student'),
      dict(Task="Wintec (Study)", Start='2017-02-15', Finish='2017-06-15', Resource='Student'),
      dict(Task="Wintec (Study)", Start='2017-07-15', Finish='2017-11-15', Resource='Student'),
      dict(Task="Wintec (Study)", Start='2018-02-15', Finish='2018-06-15', Resource='Student'),
      dict(Task="Wintec (Study)", Start='2018-07-15', Finish='2018-11-15', Resource='Student'),
      dict(Task="Wintec (Study)", Start='2019-02-15', Finish='2019-06-15', Resource='Student'),
      dict(Task="Wintec (Study)", Start='2019-07-15', Finish='2019-11-15', Resource='Student'),
      dict(Task="Wintec (Study)", Start='2020-02-15', Finish='2020-06-15', Resource='Wintec Internship'),
      dict(Task="Nyriad Intern", Start='2018-11-13', Finish='2019-02-10', Resource='Software Engineer')]

fig = ff.create_gantt(df, group_tasks=True, show_colorbar=True, index_col='Resource')

fig['layout']['shapes'].append(
{
    'type': 'line',
    'x0': present,
    'y0': -1,
    'x1': present,
    'y1': 6,
    'line':{
        'color' : 'rgb(192,192,192)',
        'dash' : 'dash'
        }
})

pl.plot(fig, filename='gantt-simple-gantt-chart', world_readable=True)
