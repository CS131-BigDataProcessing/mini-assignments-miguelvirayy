#!/usr/bin/env nextflow

nextflow.enable.dsl=2

process UPPERCASE {
    output:
    path 'output.txt'

    script:
    """
    echo ${params.str} | tr '[:lower:]' '[:upper:]' > output.txt
    """
}

workflow {
    UPPERCASE()
}
