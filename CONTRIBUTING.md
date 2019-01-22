# Contributing to prox-cli

We'd be happy for you to contribute to prox-cli.

## Support questions

Please, don't use the issue tracker for this. Use one of the following
resources for questions about your own code:

<!-- - [Gitter](https://gitter.im/hammercode/prox-cli) -->

## Project organization

* Branch `master` is always stable and release-ready.
 * **Never ever try to submit patch direcly to master**
* Branch `devel` is for development and merged into `master` when stable.
* Feature branches should be created for adding new features and merged into `devel` when ready.
* Bug fix branches should be created for fixing bugs and merged into
  `devel` when ready.

## Opening a new issue

1. Look through existing issues to see if your issue already
   exists. **So we don't have duplicate issue**.
2. If your issue already exists, comment on its thread with any
   information you have. Even if this is simply to note that you are having the same problem, it is still helpful!
3. Always *be as descriptive as you can*.
4. What is the expected behavior? What is the actual behavior? What are the steps to reproduce?
5. Attach screenshots, videos, GIFs if possible.
6. **Include prox-cli version or branch experiencing the issue.**
7. **Include OS version experiencing the issue.**


## Submitting a pull request

1. Find an issue to work on, or create a new one. *Avoid duplicates, please check existing issues!*
2. Fork the repo, or make sure you are synced with the latest changes on `devel`.
3. Create a new branch with a sweet name: `git checkout -b issue_<##>_<description>`.
4. Write unit tests when applicable.
5. Don't break unit tests or functionality.
6. Update the documentation header comments if needed.
7. **Rebase on `devel` branch and resolve any conflicts _before submitting a pull request!_**
8. Submit a pull request to the `devel` branch.


### First time setup

Please refer to [instalation](docs/instalation.md) guide.

### Running the tests

You can run the test with your own credentials

Run the basic test suite with:

``` bash
pytest
```

You can add more parameter to get more details.

``` bash
pytest --cov=prox -vv -s
```

If your test script get 'aborted' by the server. Try login manually
with `prox login` before running test.

### Running test coverage

You can generate coverage report with:

``` bash
coverage report -m
# or
coverage html
```