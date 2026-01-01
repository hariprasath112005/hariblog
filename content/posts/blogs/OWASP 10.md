
It is a regularly Updated document containing security concerns and risks for web application security, focusing on 10 most critical risks.


## Broken Access Control

- Access Control refers to a system having control to a information or functionality.
- Broken Access Controls allow attackers to bypass authorization and perform task as they were administrators.
- Access Control can by secured by making web application provide proper authorization tokens

## Cryptographic Failures

- Web applications should protect their sensitive data by using encryption.
- Or else attackers will get the data and use it for various purpose.
- The risk of data exposure can be minimised by encryption all sensitive data, authenticating all transmission and disabling caching.


## Injection

- Injection attack happens when untrusted data is sent to the code interpreter through a form input or some other way of data submission in the web application.
- A attacker could enter a sql database code into a form that expects username in plaintext. and if the form field is not properly secured, the code will execute.
- Cross site scripting is also a injection attack.
- Injection attacks can be prevented by sanitising/validating the inputs.

## Insecure Design

- Insecure Design includes a range of weakness that can be embedded in the architecture of an application.
- It focuses on the design rather than the implementation.
- For example security questions like "which street do you grew up on?" for password recovery as one example that is insecure by design.
- No matter how much the design is perfect, the system is vulnerable.


## Security Misconfiguration

- Security misconfiguration is the most common vulnerability on the list, and is often the result of using default configurations or displaying excessively verbose errors.
- This can be mitigated by removing any unused features in the code and ensuring that error messages are more general.
-  XML External Entities (XEE) attack - This is an attack against a web application that parses XML* input.
- An XML parser can be duped into sending data to an unauthorized external entity (hard drive), which can pass sensitive data directly to an attacker
- The best ways to prevent XEE attacks are to have web applications accept a less complex type of data, such as JSON


## Vulnerable and Outdated Components

- Many modern web developers use components such as libraries and frameworks in their web applications.
- Some attackers look for vulnerabilities in these components which they can then use to orchestrate attacks
- Some of the more popular components are used on hundreds of thousands of websites; an attacker finding a security hole in one of these components could leave hundreds of thousands of sites vulnerable to exploit.
- To minimize the risk of running components with known vulnerabilities, developers should remove unused components from their projects, as well as ensure that they are receiving components from a trusted source that are up to date.



## Identification and Authentication Failures

- Vulnerabilities in authentication (login) systems can give attackers access to user accounts and even the ability to compromise an entire system using an admin account.
- Some strategies to mitigate authentication vulnerabilities are requiring [two-factor authentication (2FA)](https://www.cloudflare.com/learning/access-management/what-is-two-factor-authentication/) as well as limiting or delaying repeated login attempts using [rate limiting](https://www.cloudflare.com/rate-limiting/).


## Software and Data Integrity Failures

- Many applications today rely on third-party plugins and other external sources for their functionality, and they do not always make sure that updates and data from those sources have not been tampered with and originate from an expected location
- This category also includes insecure deserialization exploits: these attacks are the result of deserializing data from untrusted sources, and they can result in serious consequences like [DDoS attacks](https://www.cloudflare.com/learning/ddos/what-is-a-ddos-attack/) and remote code execution attacks.
- To help ensure data and updates have not had their integrity violated, application developers should use digital signatures to verify updates, check their software [supply chains](https://www.cloudflare.com/learning/security/what-is-a-supply-chain-attack/), and ensure that continuous integration/continuous deployment (CI/CD) pipelines have strong access control and are configured correctly.


## Security Logging and Monitoring Failures

- Many web applications are not taking enough steps to detect data breaches. The average discovery time for a breach is around 200 days after it has happened
-  OWASP recommends that web developers should implement logging and monitoring as well as incident response plans to ensure that they are made aware of attacks on their applications.


##  Server-Side Request Forgery

- Server-Side Request Forgery (SSRF) is an attack in which someone sends a URL request to a server that causes the server to fetch an unexpected resource, even if that resource is otherwise protected
- An attacker might, for example, send a request for `www.example.com/super-secret-data/`, even though web users are not supposed to be able to navigate to that location, and get access to super secret data from the server's response.
- There are a number of possible mitigations for SSRF attacks, and one of the most important is to validate all URLs coming from clients. Invalid URLs should not result in a direct, raw response from the server.



