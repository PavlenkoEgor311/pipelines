from pipelines import tasks, Pipeline

NAME = 'test_project'
VERSION = '2023'

TASKS = [
    # tasks.RunSQL('drop table original;'),
    # tasks.RunSQL('drop table norm;'),

    tasks.LoadFile(input_file='example_pipeline/data/original.csv', table='original', columns=['name', 'url']),
    tasks.CTAS(
        table='norm',
        sql_query='''
            select *, domain_of_url(url)
            from original
        '''
    ),
    tasks.CopyToFile(
        table='norm',
        output_file='data/norm',
    ),

    # clean up:
    tasks.RunSQL('drop table original;'),
    tasks.RunSQL('drop table norm;'),
]

pipeline = Pipeline(
    name=NAME,
    version=VERSION,
    tasks=TASKS
)

if __name__ == "__main__":
    # 1: Run as script
    pipeline.run()
    # print("Все гуд")
    # 2: Run as CLI
    # > pipelines run
