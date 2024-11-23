# What I learned from CTF ENUSEC
1. [Obscurity](https://obf-io.deobfuscate.io/) when you try to hide JS source code.
2. Python Tiktoken how CHAT-GTP converts text to numbers 
3. Netcat and how it is similar to Sockets Python
4. RockYou.txt a list of the most common passwords 
5. John(John2Zip) to break into password-protected zip
6. Domain TXT record used for adding more info to domains
7. CyberChef
8. Zsteg, Stegsolve, Steghide how information can be hidden in an image not seen to the human eye. (Aperisolve)
9. How dangerous it is to use JsonWebTokens NOT securely and how to find the secret-key of JWT using Hashcat
   [common secret-keys](https://github.com/wallarm/jwt-secrets)
   ```bash
   hashcat -m 16500 -a 0 jwt_token.txt rockyou.txt
   ```
11. ChyberChef Magic function( very useful)
12. How a robot can see different things on a website by entering Bot User-Agent
13. Sherlock Tool on GitHub can look up usernames on different websites
14. Pigpen Cipher or tic-tac-toe cipher
15. [CRYPTO CIPHERS Helper](https://www.dcode.fr/cipher-identifier?__r=1.3c6fba63e378d1388d7d52ce2ee1f143)
16. ASCII to convert numbers to text
