#!/usr/bin/env python3

from aws_cdk import core

from cdk_glue_table.cdk_glue_table_stack import CdkGlueTableStack


app = core.App()
CdkGlueTableStack(app, "cdk-glue-table")

app.synth()
