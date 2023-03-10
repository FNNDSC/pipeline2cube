# plugin2cube

[![Version](https://img.shields.io/docker/v/fnndsc/pl-plugin2cube?sort=semver)](https://hub.docker.com/r/fnndsc/pl-plugin2cube)
[![MIT License](https://img.shields.io/github/license/fnndsc/pl-plugin2cube)](https://github.com/FNNDSC/pl-plugin2cube/blob/main/LICENSE)
[![ci](https://github.com/FNNDSC/pl-plugin2cube/actions/workflows/ci.yml/badge.svg)](https://github.com/FNNDSC/pl-plugin2cube/actions/workflows/ci.yml)

## Abstract

A small utility application that can register a list of ChRIS pipeline files and all dependent plugins to a CUBE instance.

## Overview

This app is a straightforward CLI tool that can be used to register a pipeline directly to a CUBE instance by using the the `chrs` and `pipeline2cube` apps.

A given pipeline (in a list) is passed to `chrs` to add to a CUBE. Any plugins in the pipeline that are not currently registered to CUBE will be returned as errors by `chrs`.

The `pipeline2cube` app will then simply parse that error information and attempt to register the missing plugin, afterwhich it will re-attempt the `chrs` operation.

In some ways, this app is akin to a Linux package installer that installs a "meta" package (a pipeline) and fetches/installs all its dependencies (plugins) if they don't exist (are not yet registered to a CUBE).

## Dependencies

The dependencies of `plugin2cube` are most pertinent, i.e. `docker` on the host for complete plugin registration. For its part `pipeline2cube` relies on `chrs` for its internal heavy lifting.

## Arguments

```html
        --pipelines <comma,list,of,pipelinefiles>
        A comma separated list of pipeline files to register. These are in either
        JSON or YML format suitable for processing the ChRIS command line client
        tool `chrs` (see https://crates.io/crates/chrs).

        Each pipeline file in turn is dispatched to `chrs` for processing, and
        any outputs from `chrs` are processed to either continue, register
        missing plugins, or abort.

        [--registry <defaultContainerRegistry>] ("fnndsc")
        The default registry organization -- assumed to be valid for all
        plugins in a given pipeline.

        [--computenames <commalist,of,envs>] ("host")
        A comma separted list of compute environments within a CUBE to which
        the plugin can be registered.

        [--CUBEurl <CUBEURL>] ("http://localhost:8000/api/v1/")
        The URL of the CUBE to manage.

        [--CUBEuser <user>] ("chris")
        The name of the administration CUBE user.

        [--CUBEpasswd <password>] ("chris1234")
        The admin password.

        [--inputdir <inputdir>]
        An optional input directory specifier.

        [--outputdir <outputdir>]
        An optional output directory specifier. Some files are typically created
        and executed from the <outputdir>.

        [--man]
        If specified, show this help page and quit.

        [--verbosity <level>]
        Set the verbosity level. The app is currently chatty at level 0 and level 1
        provides even more information.

        [--debug]
        If specified, toggle internal debugging. This will break at any breakpoints
        specified with 'Env.set_trace()'

        [--debugTermsize <253,62>]
        Debugging is via telnet session. This specifies the <cols>,<rows> size of
        the terminal.

        [--debugHost <0.0.0.0>]
        Debugging is via telnet session. This specifies the host to which to connect.

        [--debugPort <7900>]
        Debugging is via telnet session. This specifies the port on which the telnet
        session is listening.



```

## Installation

Easiest vector for installation is

```bash
pip install pipeline2cube
```

## Examples

`pipeline2cube` accepts several CLI flags/arguments that together specify the CUBE instance, pipelines to process, and several optional parameters. For a full list of supported arguments, do

```shell
pipeline2cube --man
```

To register a plugin, do

```shell
pipeline2cube                                                           \
    --CUBEurl http:localhost:8000/api/v1/                               \
    --CUBEuser chrisadmin                                               \
    --CUBEpasswd something1234                                          \
    --computenames host,galena                                          \
    --registry fnndsc
    --pipeline pipeline1.yml,pipeline2.yml                              \
    --verbosity 1

```

## Development

### Instructions for developers.

To debug, the simplest mechanism is to trigger the internal remote telnet session with the `--debug` CLI. Then, in the code, simply add `Env.set_trace()` calls where appropriate. These can remain in the codebase (i.e. you don't need to delete/comment them out) since they are only _live_ when a `--debug` flag is passed.

### Testing

Run unit tests using `pytest`. Coming soon!

_-30-_
