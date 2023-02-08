# unittest-learning-example

The goal here is to present an example of how to use unittest on an python script.

This is the main aspect of a TDD (test-driven development) approach, in which you write your test before writing the actual code. To accomplish this approach, you must follow some steps:

1 - Write tests: having a new feature, you must write a test that passes only if the new feature specifications are met. This is interesting because you have to make sure that you’ve understood all the requirements before adding it -> have to understand the requirements in order to write a good test.

2 – Run failing tests: After writing the tests, you must guarantee that they will fail. Well, if the test pass before you code the new feature (that should be tested), something is wrong.

3 – Write a ‘pass’ code: It does not need to be beautiful or clean, it just need to work. Make sure that the code adheres to the specifications.

4 – All tests must pass: New feature cant break anything. Therefore, if you have some old tests, it must attend to those as well.

5 – Refactor: Make it beautiful.

Knowing these steps, it’s presented a code that passed through all these steps, just as an example and a repo to follow if you have questions on ‘how to do it’.
