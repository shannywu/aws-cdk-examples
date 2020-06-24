from aws_cdk import aws_glue as glue
from aws_cdk import aws_s3 as s3
from aws_cdk import core


class CdkGlueTableStack(core.Stack):

    def __init__(self, scope: core.Construct, id: str, **kwargs) -> None:
        super().__init__(scope, id, **kwargs)

        self._region = 'aws_region'
        self._account_id = 'aws_account_id'

        bucket = s3.Bucket.from_bucket_name(self, 'my_bucket_id', 'my_bucket')

        database = glue.Database(
            self,
            id='my_database_id',
            database_name='poc'
        )

        table = glue.Table(
            self,
            id='my_table_id',
            database=database,
            table_name='my_table',
            columns=[
                glue.Column(
                    name='col1',
                    type=glue.Type(
                        input_string='string',
                        is_primitive=True
                    )
                ),
                glue.Column(
                    name='col2',
                    type=glue.Type(
                        input_string='int',
                        is_primitive=True
                    )
                )
            ],
            partition_keys=[
                glue.Column(
                    name='dt',
                    type=glue.Type(
                        input_string='string',
                        is_primitive=True
                    )
                )
            ],
            bucket=bucket,
            s3_prefix='test_data',
            data_format=glue.DataFormat(
                input_format=glue.InputFormat('org.apache.hadoop.mapred.TextInputFormat'),
                output_format=glue.OutputFormat('org.apache.hadoop.hive.ql.io.HiveIgnoreKeyTextOutputFormat'),
                serialization_library=glue.SerializationLibrary('org.openx.data.jsonserde.JsonSerDe')
            )
        )
