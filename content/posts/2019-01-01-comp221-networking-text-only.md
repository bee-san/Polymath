---
title: Comp221 Networking text only
slug: comp221-networking-text-only
date_published: 2019-01-01T21:00:00.000Z
date: 2019-06-19T13:52:36.000Z
draft: true
---

I# Networking revision
Hello! This is every single question asked in a lecture + more.

1. What is the transmission delay formula? Packet transmission delay = time needed to transmit L-bit packets into link = L(bits) / R(bits/sec)
2. What is unguided media? WiFi, radio - stuff that isn’t guided by a cable.
3. What is guided media? Wired stuff like Ethernet
4. If the arrival rate exceeds the transmission rate of a link within packet switching, what will happen? Packets will queue, wait to be transmitted on link. If queue is full, packets can be dropped.
5. What is routing? Determines source-destination taken by packets]
6. What is forwarding? Moves packets from routers’ input to appropriate routers output.
7. What is packet switching? Hosts break application-layer messages into packets. They forward these packets from one router to the next, across links on path from source to destination. Each packet transmitted at ful link capacity.
8. How long does it take for a packet to be pushed into the link using packet switching? L/R seconds,where L is the bits of the packet and R is the bps rate of the link.
9. What is circuit switching? End to end resources allocated to, reserved for “call” between source & dest. So with packet switching, you just send it out along a link. Circuit switching creates a dedicated link for each information you want to send out to a certain host.
10. Does circuit switching allow more users to use the network than packet switching? No. Circuit switching is a maximum of 10 users, packet switching doesn’t have a maximum. With 35 users, the probability that more than 10 are active at the same time is less than 0.0004%.
11. Why do we use circuit switching if packet switching is better? Possible for excessive congestion, packet delay and loss protocols
12. What is the ddifference between circuit switching and packet switching? Packet-switched networks move data in separate, small blocks -- packets -- based on the destination address in each packet. When received, packets are reassembled in the proper sequence to make up the message. Circuit-switched networks require dedicated point-to-point connections during calls

Packet switching breaks streams of data into smaller blocks of data. When you make a phonecall, a circuit creates a dedicated and direct link of fixed bandwidth between each node. The link lasted until the call was complete.

Packet switching lets users equally share bandwidth resources but makes no promises concerning quality or latency. Packet switching is more affordable and easier than circuit switching.

1. What are the 4 sources of packet delay? Transmission, propagation, nodal processing, queueing Best way to remember this is by using a mneomic. Like "a Teen called Nancy is not Quite Physical" transmission delay, nodal processing, propagation, queuing. Make up your own mnemonic. Mine sucks haha.
2. What is the formula for throughput? Bits / time unit, it’s the rate at which bits are transferred between sender & receiver.
3. What is the internet protocol stack? Application Transport Network Link Physical
4. What is the client-server architecture? Server is an always-on host with a permanent IP address. Clients are end-users who do not communicate directly with each other but instead communicate with the sever.
5. What is peer to peer architecture? No always on server, end users always communicate directly. Peers request services from other peers. Every peer can be a server or can be a client, or both.
6. What is a socket? A socket is like a door for communication. If you leave your bedroom door open any service (people) can come and talk to you. If you close your bedroom door (open / closing a socket) no service can communicate to you via that door.
7. Does the IP address of a host on which a process runs suffice for identifying the process? No. Many processes can run on the same IP address.
8. How do you identify a process on an IP address? IP address  / port number combo
9. What is TCP? TCP is a reliable transport protocol for sending & receiving things. It opens a tunnel from one host to another host that lets them reliably send things down it. Anything that goes into the tunnel is guaranteed to be delivered on the other end.
10. What is UDP? UDP is like sending messages via paper airplanes. The further away the person you’re talking to is, the more likely the paper airplane will fly off somewhere and get lost. UDP does not guarantee delivery of anything. The closer the person you’re talking to is the more likely it is to be delivered, but there is still alway a possibility no matter what using UDP that it won’t be delivered.
11. What’s faster, UDP or TCP? UDP is faster. In order to use TCP, you have to build a nice strong, sturdy tunnel. For UDP, you just stick it in a paper airplane and send it off.
12. What’s a good port number to choose from? Most port numbers are reserved by other processes. It’s like saying “what bedroom do you want to sleep in?” Some of the other bedrooms are occupied by Mike Tyson, Jocko Wilink, you know, the strongest people in the world kinda deal. You don’t want to set up there. Pick a port number over 2000, it’s likely to be safe.
13. Who is the client in the client-server architecture? The client is the one who will initiate the communication, server will wait to be contacted. If a server communicates with another server, the one who initiated the communication is the client.
14. Why are there 2 types of protocols for emails? What is a push / pull protocol? SMTP is the push protocol. We have an email and we want to push this to a web server, to a repicent. We have the information and we want to push it somewhere. The last one was the mail access protocol. IMAP or POP3, we communicate to a web server to pull the email from the server as our computer isn't always on.
15. What is non-persistent HTTP? Non persistent HTTP means that once a request has finished, close the connection. At most, one object can be sent over the TCP connection. Downloading multiple objects requires multiple connections.
16. Does HTTP/1.0 use persistent HTTP? No, it uses non-persistent HTTP.
17. What is persistent HTTP? Multiple objects can be sent over single TCP connection between client and server. With non-persistent HTTP, after one request is finished it closes the tunnel. With persistent HTTP, it never closes the tunnel until its explicitly told to close it.
18. Does HTTP/1.1 use persistent HTTP? Yes, it does.
19. What is RTT? Round trip time. The time it takes for a small packet to travel from client to server and back.
20. What are the two types of HTTP messages? Request, Response
21. What is a DNS? Domain name server. Basically you have a bunch of names, like Yahoo, Google, Amazon which are readable by humans. But these aren’t readable by machines. When you write “Amazon” into the URL bar your machine asks the DNS what the address of Amazon is. The DNS than returns something like 174.57.182.1.
22. Is there a set-in-stone DNS for every name : address translation out there? Nope. It doesn’t scale well, it’s a single point of failure and too much traffic. There are multiple DNS’.
23. Suppose a webpage consists of many small pictures. You have the choice of two browsers - one persistent HTTP and one non-persistent HTTP, what one do you choose? Persistent HTTP. The way photos work in web pages is that they’re often not included in the HTML / CSS / JavaScript you download from a website. This means that for every single picture you’ll have to download each one. Persistent HTTP is better used here since you have to download many things.
24. How much time does it take to distribute file (size f) from one server to N peers? Assume D is the minimum download rate. F/d is the minimum client download time. F/u is the time to send one copy. NF/u is the time to send N copies. Then: Max{NF/u, F/d} This probably won’t come up in the exam.
25. What are the sizes of chunks in Kb which BitTorrent divides a file? 256Kb per chunk
26. Alice is using the BitTorrent client to pirate Photoshop. Alice has 8 peers sending her chunks of the Photoshop file. Those 8 peers are also pirating Photoshop. What peers does Alice send the chunks to at the highest speed possible? The *4* peers who are sending her chunks at the highest possible rate.
27. What happens to the other 4 peers? They are ‘choked‘ by Alice. They do not receive any chunks from her.
28. How long does it take for Alice to re-evaluate her top 4 peers? Every 10 seconds
29. If you have 6 peers, 4 peers sending chunks at 50Mb/s and two peers sending at 1Mb/s, would the two peers ever complete their download? Yes. Every 30 seconds BitTorrent randomly selects another peer (speed doesn’t matter for this one) and starts sending them chunks. Alice ‘optimistically unchokes’ this peer. If Alice enters the peers top 4 senders, that peer may enter Alice’s top 4.

BitTorrent is known as a ‘tit-for-tat’ algorithm. The higher your upload rate (the more you share), the higher your download rate is. If you limit your upload rate, you’ll download slower. But, you will download - you won’t be ignored completely.

1. Why is TCP unreliable? Generally, it isn’t. This is a trick question.
2. How many handshakes does UDP perform before it connects with a server? None, it just sends it. Imagine the doors and paper airplanes. With a door, you knock before you enter. With paper airplanes, you just lob them and hope the person catches them.
3. If you send 2 UDP packets, can they arrive in different orders? Yes! Absolutely. Imagine you and your friend made 2 paper airplanes. Your friend is shit at them, so his airplane goes slower than yours - despite him throwing it first. It’s entirely possible for UDP to have 2 packets arrive in different orders.
4. What are packets called in UDP? Ok ok ok, so UDP calls packets ‘datgarams’ but in his slides he calls them Packets most of the time, so like just keep this in mind okay?
5. Why is it said that FTP sends control information ‘out-of-band’ Ok so, he doesn’t answer this in the lecture but out of band means a dedicated channel is used. In FTP, two TCP sockets are opened. One for transmitting / receiving data and one for session related commands like session setup, directory navigation. The use of the second socket is out of band communication.

Also, he said in the lecture on the 11th of October 2018 that, and I quote, “FTP will not be in the exam”. So dw about this.
47. Consider an HTTP client that wants to retrieve a web document at a given URL. The IP address of the HTTP server is initially unknown. What transport and application layer protocol are needed in this scenario?
DNS to get the IP address, HTTP to get the hTTP object. They both build on the transport layer protocols. HTTP builds on TCP. In default mode, DNS uses UDP as we want DNS to be quick and fast.
48. Why do HTTP, FTP, SMTP run on top of TCP rather than on UDP?
Because they all contain data that the user sees directly. We don’t want this to be corrupted. If we go to a bank webpage we want to make sure the connection is secure and we can trust what we are seeing.
49. List the four broad classes of services that a transport layer protocol can provide
* Reliable data transfer: TCP
* A gurantee that a certain value for throughput will be maintained: Neither TCP nor UDP
* A gurantee that data will be delivered in a specified amount of time: Neither TCP nor UDP
* Security: Neither TCP nor UDP
50. In class we discussed a UDP server and a TCP server. The UDP server needed only one socket, whereas the TCP server needed two sockets. Why?
two TCP sockets are opened. One for transmitting / receiving data and one for session related commands like session setup, directory navigation. The use of the second socket is out of band communication.
51. If the TCP server were to support N simultaenous connections, how many sockets would the TCP server need?
TCP needs 2n sockets, where n is the number of simultaenous connections.
52. What does the transport layer do?
Provide logical communication between apps running on different machines.
53. What is multiplexing?
Multiple signals are combined into one signal to be sent over a shared medium.
54. What is demultiplexing?
Taking the one multiplexed signal and converting it back into many different signals
55. What is the goal of a checksum?
To detect errors in a transmitted segment
56. How does a checksum work?
Sender treats all the content of the segment as 16-bit integers, including the header fields. They then calculate the 1’s complement sum of all of the segments contents. They put this checksum into the UDP checksum field. Note: TCP automatically does checksumming, so it’s not useful for TCP.

The receiver then computes the checksum of the received segment much like how the sender did it. If the computed checksum equals the checksum field value then no error is detected (kind of... the checksum field itself could be corrupted). If they don’t equal, corrupt has occurred.
57. Compute the checksum of these two numbers:
**111001100110110**
**1101010101010101**
So the sum is:
11011101110111011
But this is 1 digit too long, so we wrap it around. We know it’s 1 digit too long because it’s supposed to be 16 bit. When we wrap around, we take the most significant bit (which is the 1 at the start) and we add that to the back - a carry out as he calls it.
1011101110111100
We had this at the back:
011
When we add 1 to the back, we get:
010
Now the 1 moves forward, because 1 + 1 = 0 and that extra 1 has to go forward
000
Now we move the 1 forward again:
100
58. What’s more important, reliable data transfer or the speed of that transfer?
Well, they’re both important - but Martin said that you can have the fastest paper airplane in the world (UDP packets) but if it doesn’t arrive at its destination properly than it doesn’t matter.
59. What is an RDT protocol?
Reliable data transfer protocol. Most of this is assginment 1, but I’ll go over the things more likely to be in the exam.
60. How does a receiver tell the sender that the packet is not okay, IE it’s corrupted?
ACK (acknowledgement) says “the packet is okay”. NACK (negative acknowledgement) says “the packet is not okay, it’s corrupted”.
61. What if the sender sends back NACK, but that NACK packet is corrupted?
The receiver has no idea what happened so they just kill themselves and hope the sender uses TCP in the future. Just kidding.

The sender sends the packet a second time, but this time with a sequence number. If the receiver receives the packet again, but the packet was perfectly fine the first time - nothing wrong with it,then they’ll ignore this packet and send back ACK.

If the package was corrupted the first time round, they’ll send back ACK / NACK depending on whether the new package is corrupted or not.

Either way, the sender sends one packet then waits for response. This is called a stop and wait protocol.
C
62. How does RDT2.2, a NAK free protocol, work?
Same functionality as rdt2.1, but only using ACKs. Instead of NAK, receiver sends the ACK for last packet that was received okay.

So let’s say I send you 2 packets, and they’re in a vector like so: (content, seqNum):

(“Please I need divine intervention to pass AI”, 0)
(“Submitted coursework for comp221”, 1)

The receiver than sends back “okay, ACK for seqNum 0. That packet was received all okay and that was the last packet I received”

Now, the sender knows that that’s not the last packet they sent, so something must of gone wrong. They resend all the packets from the last okay packet back to the receiver.

1. How do we deal with the fact that ACK’s can get lost in the network? The sender waits a ‘reasonable’ amount of time for ACK. If no ACK, retransmit.

If the ACK is delayed,the retransmitted will be duplicated but the seqNum will tell the receiver to ignore it.

1. What is a pipeline protocol? The sender allows multiple, ‘in-flight’, yet to be acknowledged packets to go over the network.
2. What does full duplex mean? It means that the data can flow both ways at the same time. With a telephone or a normal human conversation you can’t talk at the same time as your time is talking. This is called half duplex. Full duplex is just the rudest thing ever, just talk over everyone at the same time on the same device who cares?
3. Is it possible for an application to have reliable data transfer over UDP? Yes, this was assignment 2.
4. How does TCP know when packets are received in a different order to the way they were sent? Sequence Numbers
5. How does TCP handle out-of-order segments? TCP specification doesn’t say, it’s up to the programmer
6. How does TCP set the timeout value? “Well, it’s longer than round trip time.” “But, how long is round trip time Martin?” “It depends, okay moving on....”
7. How do you estimate the RTT? You sample it. Measure time from segment transmission until ACK receipt. But it’ll vary a lot. We want the average RTT.
8. What is flow control? The receiver controls the sender, so sender won’t overflow receivers buffer by transmitting too much.
9. How does flow control work in TCP? Receiver advertises free buffer space by including **rwnd** value in TCP header of receiver-to-sender segments. The **rwnd** is the receiver buffer size which is set by socket options (default is 8192 bits).

The sender limits the amount of unasked “in-flight” data to receivers **rwnd** value.

This guarantees that the receive buffer will not overflow.

1. Before sending data in TCP, what happens? The sender & receiver handshake. This is an agreement to establish connection, and they agreed nt he connection parameters.
2. Will a 2-way handshake always work? Martin sends Boris an email: “can we talk?’ Boris sends back “yes, of course” Martin than forgets about his meeting with Boris, or he gets preoccupied suddenly, or something bad happens and he can’t attend. Since this is a 2-way handshake, he can’t tell Boris this.

This is where a 3-way handshake comes in. When Boris says “yes, of course” Boris sprints to Martin’s office faster than the speed of light - so fast that it is literally impossible for Martin to forget or delay the meeting.

In networking, this is just the establishment of the connection. The sender doesn’t establish the connection in a 3-way handshake, the receiver does.
75. How does a TCP connection close?
Someone sends back a TCP segment with the **fin** attribute set to 1. The receiver sends back **fin** with an **ack** attached to it.
76. What is congestion in networking?
Informally: “too many sources sending too much data too fast for the network to handle”.
This is different from flow control. Martin ranks this as networking’s biggest problem.

1. How does end-end congestion control work? No explicit feedback from network, congestion inferred from end-system observed loss. Approach taken by UDP. Discussed more soon.
2. How does network-assisted congestion control work? Routers provide feedback to end systems Single bit indicating congestion flipped in header of segment Explicit rate for sender to send at, limiting the rate a sender can send data at will slow down the network, making congestion go down.
3. How does TCP congestion control work? Sender increases the transmission rate for usable bandwidth until loss occurs. So when people are sending things too fast, they let them send things faster. Doesn’t make sense so much.

Additive increase: increaes **cwnd**  (congestion window) by 1 **mss** every RTT until los detected.
Multiplicative decrees: cut **cwnd** in half after every loss.

Note: I forgot to do the complement here. Take all0s as 1s and all 1s as 0s.
86. Why do UDP and TCP take the 1s complement?
The receiver takes every single bit, sums them up. We add to the sum the co,mplement of the sum and it should give us a string of only 1s.

We add the sum and the checksum which gives us a string entirely of 1s. He’s going to ask us in an exam whether 2 checksums are right using this method.

It’s probably best to use an example. If you’ve brought the course textbook, you’ll know for each section (transport, physical, cyber security etc) you can go online and download an exam for that section (but only if you’ve brought the book). This question and it’s answer comes from that exam, from the book.

    0110011001100000
    0101010101010101
    1000111100001100
    

UDP at the sender side performs the 1s complement of the sum of all the 16-bit words. The sum of first two of these 16-bit words is

    0110011001100000
    +
    0101010101010101
    --> 1011101110110101 
    

Adding the third word to the above sum gives, Note that this last addition had overflow, which was wrapped around

    --> 0100101011000010
    

The 1s complement is obtained by converting all the 0s to 1s and converting all the 1s to 0s.
Thus the 1s complement of the sum 0100101011000010 is 1011010100111101, which becomes the checksum. At the receiver, all four 16-bit words are added,including the checksum. If no errors are introduced into the packet, then clearly the sum at the receiver will be 1111111111111111. If one of the bits is a 0, then we know that errors have been introduced into the packet.

    0110011001100000
    +
    0101010101010101
    +
    1000111100001100
    +
    1011010100111101
    —-> 1111111111111111
    
    

Martin said in a lecture (I have it written down, but not what lecture it was) that he’s going to give us a complements checksum and some numbers and he’s going to ask us whether or not there was any errors (it’s not all = 1). He said he’ll likely use, and I quote “not 16 bit as thats too hard. 4 bit maybe? No, that’s too easy. Likely 8 bit”

What I’ve shown above is essentially what is going to be in the exam, except 16 bit.
87. In our RDT protocol, why did we need to introduce timers?
If the sender sends a packet and receives no ACK / NACK after a period of time, it’s useful to assume that something bad has happened so after the timer it resends the packet. z
88. Why did we introduce sequence numbers in our RDT protocol?
Let’s say you have 2 servers, one of them called Apple and the other called Microsoft.
Micrsoft sends Apple a datagram containing the words “please help us sell phones”. Apple replies back “sure, we’ll send you the documents now. Just getting our secretary to do it” but this reply gets lost and doesn’t arrive at Microsoft.

Microsoft, after let’s say 5 minutes, decides something went wrong and sends it again. Apple replies the same thing. Now their sectrarties have 2 of the same thing to do.

We introduce sequence numbers so Microsoft can say “hey, i sent packet number 13262 to you 5 minutes ago. Here’s the exact same packet”. Apple will see that it’s the same due to the sequence numbers and won’t ask their secretaries again.
89. The internet is described as an unreliable communications medium.
1. What chareecteristics of internet communication lead to this description?
UDp. Packets don’t arrive in the order sent, packets sometimes don’t arrive at all.
2. Which protocol was developed to deal with these undesierable features?
TCP
3. Explain how the features of this protocl address the issues listed in 89)1.
Packets always arrive in the order they were sent (actually, they’re not. But it’s super easy to put them into the right order once you have them). Packets are guranteed to arrive at destination.\

1. True or False?  Supose  host A is sending a large file to host B over a TCP connection. If the seq number for a segment is **m**, then the seq number of the subsecuent segment is neccersaily **m+1**. Not true. In UDP it’s common to do m + 1 as you want them to be aware of the order of packets and stuff. Say you sent 3 packets with seq numbers, 1, 2, and 3. If they only recieve 1 and 3, they know that 2 is missing.  

In TCP, packets are always delivered so the seq number is derived by the amount of data in the segment.
2. The number of unacknowledge bytes that A sends cannot exceed the receive buffer
True. This is called flow control. In our ACK / NACK we always say how much is left in the recieve buffer to make sure the sender doesn’t overflow our buffer.
3. The size of the TCP receive window (**rwnd**) never changes throughout the duration of the connection.
False. TCP has 2 sockets, 1 for data and 1 for management. Through this management socket, you can change the size of the **rwnd** depending on many factors such as how many other clients are connectec to the server.
4. The TCP segment has a field in its header for **RWND**
True.  See below for an ASCII diagram of all the TCP headers.

                                        
        0                   1                   2                   3   
        0 1 2 3 4 5 6 7 8 9 0 1 2 3 4 5 6 7 8 9 0 1 2 3 4 5 6 7 8 9 0 1 
       +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
       |          Source Port          |       Destination Port        |
       +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
       |                        Sequence Number                        |
       +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
       |                    Acknowledgment Number                      |
       +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
       |  Data |           |U|A|P|R|S|F|                               |
       | Offset| Reserved  |R|C|S|S|Y|I|            Window             |
       |       |           |G|K|H|T|N|N|                               |
       +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
       |           Checksum            |         Urgent Pointer        |
       +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
       |                    Options                    |    Padding    |
       +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
       |                             data                              |
       +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
    

Since a question like this has come up, I suggest drawing the TCP / UDP packets and sticking them somewhere you’ll see them, like on a mirror. ]
5. Suppose host A sends one segment with seq number 38 and 4 bytes of data over a TCP connection to host B. In the sames egment, the ack number is neccasrily 42.
False. Ack number and seq number have nothing in common. 42 is the ack number.
91. Alice sends a message to Bob which is 4500 bytes long, and is broken into segments of 1000 bytes each. Alice chooses a random start value of 3300 for her sequence numbers.
1. How many segments will the message be broken into?
4500 / 1000 = 4.5, round up to 5 segments.
2. Give the start and end bytes of each segment
So we start off with the start value of the seq number, so the first byte is:
3300 the end byte is (start byte + segment length) - 1. So the end byte would be 4299. This is because the next segment starts at (start byte + segment length), as seen below. Also, we know there are 5 segments (first part of the question)
3300 - 4299
4300 - 5299
5300 - 6299
6300 - 7299
7300 - 8299
3. Give the ACK numbers which bob will use to indicate that each segment was received uncorrupted
The ack number is how much data was received, so it’s the end byte + 1.
4300, 6300, 6300, 7300 and then because we have one more segment at the end which starts at 7300, 8300.
4. Suppose Bob chooses a random start of 217 for the sequence numbers of his ACKs. And that he only sends headers (and no data) back to Alice. What will the ACK numbers used by Alice in response to these ACKs be?
All of them will have ACK numbers of 217. The program can’t use the size of the data, as there isn’t any data. The only other way to identify a packet is using it’s SeqNum, so all of the packets will have 217.
5. Draw a brief message sequence chart for this interaction.
The MSC should show two vertical lines, one representing Alice and one Bob, with time running down the page. Between the two lines are diagonal arrows representing each message sent by either party, in sequence order, with each arrowhead pointed towards the receiver of the message. Each arrow should be annotated with the sequence numbers or ACK numbers corresponding to that message which the arrow represents.

1. A hacker breaks into your network, what are some of the things they can do? Eavesdrop - intercut messages. Impersonation - pretend to be you. Man-in-the-middle attack - insert / modify messages being sent Hijacking - remove sender or receiver and put themselves in that place Denial of service - prevent service from being used by others
2. How does the Caesar cipher work? You pick a key, such as key = 1. You map the alphabet out, so a = b, b = c, c = d and so on (this is using key = 1. If key = 2, a = c, b = d etc. For a total of 25 keys). You then rewrite the message out using this new alphabet.
3. How effect would a Caesar cipher key of 26 be? Not very. A key of 26 would mean that a = a, b = b, c = c, d = d and so on...
4. What is symmetric key cryptography? Bob and Alice share the same (symmetric) key, K_a-b.

The key is the alphabet shift in Caesar cipher. Bob and Alice will have to agree on this key before they start communicating.

1. What is a monoalphabetic cipher? Similar to Caesar cipher, except no fixed pattern of substitution. With Caesar, it was a key of 3, a key of etc. With monoalphabetic, the alphabet is chosen randomly. So a = a, b = f, c = p and so on, completely random.
2. How many different pairings are there in the monoalphabetic cipher? 26!
3. How would you break a monoalphabetic cipher? Statistical anaylsis. So ‘e’ counts for 13% of the letters in a sentence, ‘t’ for 9%. Do this for every single letter. In the encrypted text, find the letter thats worth 13% and assume that’s ‘e’. This is called Zipfs law, VSauce made a good video on it.
4. How secure are monoalphabetic ciphers? Not very. If Trudi knows the words ‘alice’ and ‘bob’ are in the plaintext (non encrypted text), then. Given the ciphertext she can determine the mapping of 8 letters.
5. How does the polyalphabetic cipher work? For every letter in the plaintext, use a different monoalphabetic cipher. So for dog, use M_1 (monoalphabetic 1) for D, M_2 for o, M_3 for g.
6. What are some ways of breaking encryption? You have cipher-Text only attacks. This is where you only have the ciphertext, you can try to brute force this or use statistical methods. Known plaintext attacks is where you know some of the **(plaintext, ciphertext)** pairings. Chosen-plaintext attacks means that you have a function, c(x) and this function encrypts x in the cipher. Easiest way is to choose to encrypt c(“the quick brown fox jumps over the lazy dog”) and you get a nice mapping of each letter.
7. What are the two types of symmetric ciphers? Block ciphers, stream ciphers.
8. What is a block cipher? Break plaintext message into equal size-blocks
9. What is a stream cipher? Encrypt one bit at a time
10. How does a stream cipher work? You combine each bit of a key stream with a bit of plaintext to get a bit of ciphertext.

So we break it down to blocks of 3. 010 = 101. 110 = 000. And so on.
108. How many possible mappings are there for K = 3 in a block cipher?
2^k mappings
109. In a block cipher, how many possible permutations aretherefor 3 bit input?
So there’s 2^3 mappings, which is 8. Then 8! Is 40,320.
110. In the prototype function for cryptography,why do we use rounds?
If only asingle round, then one bitof input affects at most 8 bits of output. In 2nd round, the 8 affected bits get scattered and inputted into multiple substitution boxes.
111. Why do we not split a message into 64-bit blocks and encrypt each block seperately?
If the same block of plaintext appears twice, it will give thesame ciphertext. This is a pattern that the attacker can use to exploit your crypto.
112. How does public key cryptography work?
You have 2 people that way to talk to eachother. Alice encrypts her message with bob’s public key. As the name implies, this key is public - anyone can access it.

When bob receives this message, he adds his private key to it. This private key reveals the plaintext. Yeah, I know. If you’ve never heard of this before you’ll think I’m making stuff up. What’s next Brandon? Cows start their own makeup YouTube channels on the moon while Xiaowei tries to teach them AI?

Don’t believe me? Google it. This shit is some magic.
113. Is [(a mod n) + (b mod n)] mod n = (a + b + n)?
No, it’s equal to (a + b) mod n. Sorry, if I don’t confuse you with the question your brain will trick you into thinking you know it.
114. Okay, so if that’s equal to (a + b) mod n, does that mean that [(a mod n) - (b mod n)] mod n = (a - b) mod n?
Yes, it does. No tricks here ;)
115. Okay, does that work for multiplying as well?
Yes, it does. It’ll be equal to (a * b) mod b
116. Did I just lie on the answer before this question?
Yes, I did. Another trick! It’s equal to (a * b) mod n, not mod b.
117. How do we choose keys in RSA?
1. Choose 2 large prime numbers, p & q
2. Compute n = p*q*
*3. Compute z = (p-1)(q-1)*
*4. Choose e (with e < n) that has no common factors with z*
*5. Choose d such that e*d - 1 is exactly divisble by z
6. Public key is (n, e) and private key is (n, d)
118. How do we encrypt using RSA now that we have keys?
Given (n, e) and (n, d) as computed above
1. To encrypt bit pattern m, compute:
$$ c =m^e mod n $$
2. To decrypt recieved bit pattern, c, compute:
$$ m = c^d mod n$$
119. Bob chooses 2 numbers p = 5, q = 7. What is n and what is z?
N = 35, z = 24
120. What is e and what is d?
E = 5, d = 29
121. Say we have a message such as 0001100, this is 12 in base 10. Calculaate $m^e$
It’s 248832
121. What is $c = m^e mod n$ ?
It’s 17.
123. Now decrpyt it. What is $c^d$?
It’s 4819.... tbh i’m not even going to write this out lol i can’t copy and paste because i’m reading this pdf in an image editor lmao
124. What is $m = c^d mod n$?
12
125. So if privateKey(publicKey(m)) == m, then does publickey(privateKey(m)) == m too?
Yes, they all equal each other!
126. Just a note, no tricks or quesitons here. He talks about authenitcation next but all of his slides lead up to the idea that we can use public key cryptography for authentication, but he doesnt show us any examples or anything so i’m ignoring these as it likely wont come up.
127. What is message integrity?
Allows communicating parties to verify that received messgeas are authentic, from the person who sent them.
128. What is a digital signature?
Much like a physical signature, but digital.
129. How is public key cryptography used in digital signatures?
Let’s go back to this formula:
$$k^-_b(k^+_b(m)) = m = (k^+_b(b^-_b(m))$$

If Bob signs a message with his private key, then anyone can use his public key on that message and get the plaintext back. Since only Bob has his private key, anyone can prove that the message came from Bob.

As a side note: This is perfectly valid and has been used in court many times to prove that a message came from someone.

1. Signing large messages is slow, how do we speed it up? Use a hash function which creates a fixed size digest of the message, H(m)
2. What is a certification authority? It binds a public key to a specific entity. So Trudy (the attacker) sends a pizza store a request for 4 pepperoni pizzas. She signs this request with her private key,

She then sends her pizza store her private key and says it’s Bobs private key.

The pizza store believes her and sends Bob 4 pepperoni pizzas, which he didn’t order.

Bob doesn’t even like pepperoni.

A certificate authority binds a public key to a particular entity, E. The certificate authority signs the public key.

When Alice wants Bob’s public key, Alice gets Bob;s certificate from the CA and applies CA’s public key to Bob’s certificate to get Bob’s public key.

1. Alice wants to send Bob a secure email without her husband knowing. How would Alice have an affair with her husband without him being able to decrypt the emails? Alice generates a random symmetric private key, $k_s$ She encrypts the email “my husband thinks our child is his, but it’s actually yours” with the key $K_s$ (for efficiency) She also encrypts Bob’s $K_s$ with Bob’s public key Sends both $K_s(m)$ and $K_b(k_s)$ to bOB

Bob uses his private key to decrypt and recover $K_s$
Bob uses $K_s$ to decrypt and recover M
Bob has been missing for over 14 years, no one has heard from him since.

1. Alice wants to provide sender authentication to prove the message came from her and not her husband, what does she do? She digitally signs the message and sends both message (in the clear) and digital signature

Alice uses 3 keys. Her private key, Bob’s public key, newly created symmetric key

Alice’s husband is concerned with the fact she is using bank-level encryption to message her friend, Bob.

This is all a protocol called Pretty Good Privacy btw
134. What is the network layers purpose?
Transport segment from sending to receiving host. On the sending side it encapsulates segments into data grams. On the receiving side it delivers segments to transport layer.

On the receiving side, delivers the segment to the transport layer.

1.  When looking for the forwarding table entry for a given destination address, how does longest address prefix work? Say you have 2 addresses in the table: 11011000 and 110011111 Your destination address is 1100, where do you send it to? The second one, because we match the longest prefix. 
2.  What are the three types of switching fabrics? Memory, bus, crossbar 
3.  How does switching via memory work? Traditional computers with switching under direct control of CPU. Packet copied to system’s memory, speed limited by the memory bandwidth. 
4.  How does switching via a bus work? Data gram from the input port memory to output port memory via a shared bus. 
5.  What is bus contention? The switching speed is limited by the amount of bus bandwidth. 
6.  With a data gram, how many bytes are reserved for TCP headers or IP headers? 20 bytes. 
7.  What is MTU? The maximum transfer size, you often split datagrams up based on their MTU. 
8.  You have a 4000 byte datagram and a 1500 byte MTU, how much do you split it up? 3 datagrams. First one is size 1500, second one is size 1500. Because each packet reserves 20 bytes for headers, the amount of data the first two can hold is actually 1460. That leaves us with 1040 bytes left to go, which we send at the end in a third packet. 
9.  How many bits is a normal IPV4 IP address? 32 bits. 
10.  What is a subnet? It’s a section of an IP address. Device interfaces with the same subnet part of an IP address. They can physically reach each other without going to a router first. 
11.  How do you determine the subnets? Detach each interface from its host or router, creating islands of isolated networks. Each isolated network is called a *subnet*. 
12.  How many subnets?  

6, as each router is connected to one another and creates its own subnet.
147. How does Classless InterDomain Routing work?
Lol what kind of name is that. But anyway, the subnet portion of the address is of arbitrary length. Normally the IP address looks like this:
A.b.c.d/x
Where a, b, c, d are the IP address parts and the x is the subnet.
148. How does a host get an IP address?
Can be hard coded by the system admin in a file, but is usually assigned dynamically. This means that every time the device comes online it gets a new IP address.

The protocol for giving ip addresses is called the Dyanmic Host Configuration Protocol (DHCP), it dynamically gets it from a DHCP server.

1.  Give an overview of how DHCP works (as in, say what the device does to get an IP address and say what the server responds with) Device broadcasts “DHCP discover” message, to find a DHCP server DHCP server responds with “DHCP offer” Host requests an IP address “DHCP request” DHCP responds “yeah but only if u give me mcdonalds xxx” DHCP actually responds “DHCP ack” to say Yes 
2.  Can a DHCP server return 2 IP addresses to the host that wants an IP address? Yes, weirdly enough it can. It can return the IP addresses of: 

    * The first router for the client
    * Name and IP address of a DNS server
    * Network mask (indicating network versus host portion of address)
    

1. How does a network get the subnet part of an IP address? It gets allocated a portion of its providers ISP address space.

---

1. How does an ISP get blocks of addresses? Internet Cporation For Assigned Names and Numbers (ICANN)
2. What does NAT stand for? Network address translation
3. So... wtf is a nat? Your router has one IP address, as an example 138.76.29.7. All of your devices on this router have local IP addresses such as 196.168.0.1.

All datagrams leaving the local network have the same single NAT IP address, but different source port numbers.

1.  In an IPv6 datagram, how large is the header? It’s 40 bytes. Also, fragmentation isn’t allowd with IPv6. 
2.  What are some of the big changes from IPv4 to IPv6? Removed the checksum to reduce processing time at each hop. 

Options are allowed, but are indicated by the next header field.

New version of ICMP: ICMPv6

1.  How does a network deal with both IPv4 and IPv6? It uses something called tunneling, An IPv6 datagram is carried as a payload in IPv4 datagram among IPv5 routers. 
2.  What’s a flow table? Each router contains a flow table that is computed and distributed by a logically centralised routing table. 

The flow is defined by header fields. Here are some simple packet-handling rules:
* pattern: match values in packet header fields
* Actions for matched packet: drop, forward, modify, matched packet or send matched packet to controller
* Priority: disambiguate overlapping patterns
* Counters: num of bytes or num of packets

1. What are the 2 main functions for the network layer? Forwarding: moving packets from router;s input to appropriate router output

Routing: determine router taken by packets from source to destination

1. Explain how per-router control plane works Individual routing algorithm components in each and every router interact with each other in the control plane to compute the forwarding table.

Forwarding tables are tables of {name: IP address} so they know where to forward things to.

1.  What is a logically centralised control plane? A distinct controller interacts with local control agents in routers to compute the forwarding tables. So instead of every router computing it, now one big organisation computes it. 
2.  What is the goal of the routing protocol? Determine good path through the network from source to destination 
3.  What is global information in a routing algorithm? All routers have complete topology, link cost info. They also have link state algorithms. 
4.  What is decentralised information in a routing algorithm? Router knows physically-connected neighbors, link costs to neighbors. 

Iterative process of computation, exchange of info with neighbors.

Uses distance vector algorithms.

1.  What is static routing? Routes change very slowly over time. 
2.  What is dynamic routing? Routes change more quickly than static. Periodic updates to the route. In response, the link cost changes. 
3.  What are the regions called that we aggregate rout3ers into? Autonomous Systrems (AKA domains) 
4.  What is intra-AS routing? Routing among hosts, routers in same AS (network) 

All routers in AS must run same intra-domain protocol.

Routers in different AS can run different intra-domain routing protocol

Gateway router at the edge of its own AS, has links to routers in other AS’es.

No idea what this means, but it’s a thing that exists.

1. What is OSPF? Open shortest path first. Open means its publicaly available. It uses the link-state algorithm.

Router floods OSPF link-state advertisements to all other routers in the entire AS.

1.  What is ISIS routing? Please don’t blacklist me Mr. CIA man ISIS is ‘identical to OSPF’ according to the lecturer but he doesn’t say what ISIS stands for... 
2.  What is BGP? Border Gateway Protocol, the glue that holds the internet together. The de facto inter-domain routing protocol 
3.  How does BGP work?  
4.  What are some important attributes of BGP? When sending a list of ASes through which prefix advertisement has passed, we use AS-PATH. No idea what this means?? But ok thanks martin. 

NEXT-HOP: Indicates specific internal-AS router to next-hop AS.

TBH i don’t know this stuff very well.

1.  What is policy-based routing? Gateway receiving route advertisement uses import policy to accept / decline path 
2.  What is software defined networking? Internet network layer has historically been implemented by a distributed, per router approach. 

A monolithic router contains switching hardware, runs properitary implementation of internet standard protocols in proprietary routers.

Different routers for different things

SDN is a logically centralised control plane. Easier network management, avoiding dns controller configuations, greater flexibility - the lot.

It allows “programming” routers, centralisation of programming is easier and most of it is open source!

1.  What if the network operator wants u-to-z traffic to flow along a different path, such as u-v-w-z? We need to define link weights so traffic routing algorithm computes routes accordingly (or need a new routing algorithm). This is highly complicated. We don’t want to use link weights as control knobs. 
2.  What if the network operator wants to split up u-to-z traffic along -u-v-w-z and u-x-y-z (load-balancing)? We can’t do it (or we need a new routing algorithm) 
3.  What if we want to route 2 types of traffic differently? Can’t do it (with destination based forwarding, and LS, DV routing) LS is link space, DV is distance vector. 
4.  What is a data plane switch? Fast, simple commodity switches implementing generalised plane forwarding in the hardware. 

Switch flow table computed, installed by the controller.

API for table-based switch control (OpenFlow)

1.  How does the SDN controller (network OS) work? Maintain network state information, interacts with the network control applications “above” via northbound API. 
2.  What is an SDN control app? It’s the brains of control, implementing control functions using lower-level services, API provided by SDN controller. 

Unbundled can be provided by 3rd party: distinct from routing vendor or SDN controller.
182. What is the openFlow protocol?
Operates between controller and the switch. TCP is used to exchange messages.

1. What are the 3 classes of OpenFlow messages?

    * Controller-to-switch
    * Asynchronous (switch to controller)
    * Symmetric
    

184. What are the different names of packets, and what order do they go in?
Message encapsulation
Segment
Datagram
Frame

In that order (not to sure on encapsulation but he said it out loud in the lecture)

1.  In the link layer, what are hosts and routers called? Nodes 
2.  In the link layer, what are communication channels that connect adjacent nodes called? Links 
3.  What is a packet called in layer 2? Frame, it encapsulates the datagram 
4.  What is the responsibility of the data-link layer? Transferring datagram from one node to physically adjacent nodes over a link 
5.  Does the link layer remove errors? No, it may or may not provide RDT over link. 
6.  When encapsulating a datagram into a frame, what is added? Add a header and a trailer (similar to checksum at the end of a frame). Channel access if it’s a shared medium. 
7.  Does the MAC address ever change? No, it doesn’t. 
8.  Why do we need both link-level and end-end reliability? “We can fix locally at link layer” - 14 minutes into the lecture on 16/11/18 
9.  What is noise? Lots of things generating electro-magnetic noise. 
10.  Is it possible to correct errors without retransmission in the link layer? Yes, it is! 
11.  Where is the link layer implemented? In the adaptor aka the network interface card (NIC) or on a ‘chip’ 
12.  Explain how 2 adaptors communicate: Sending side: 

    * encapsulates datagram in frame
    * Adds error checking bits, rdt, flow control etc
    

199. With a multiple access protocol and a broadcast channel of rate R bps, what is the average send rate?
R/M - where M is how many nodes there are.
200. What is TDMA?
Basically, if you spam everything down one channel you gonna get congestion, so we split it up into multiple channels so there isn’t congestion. It’s like making a 2 lane motorway into a 4 lane motorway because its so busy.
Time division Multiple Access. This is some call of duty future shit right here.Well, it sounds like it.

Access to channel in rounds. Eeach station getsa fixed length slot

Unused slots go idle.

A 6-station LAN, 1,3 ,4 have packets, slots 2, 5,6 are idle

We say the utilisation rate is 50%, as only half are used.
201. What is cyclic redundancy check?
More powerful error-detection coding. View data bits, D, as a binary number.
Choose r + 1 bit pattern (generator) G.

202. What is FDMA?
Frequency doggo multiple access
Division*

The channel spectrum (basically a special way to say that every new motorway of the channel) is divided into frequency bands

Soo with TDMA you have everything on the same freq. imagine you’re using FM radio with the freq 107.8, you travel from Liverpool to Manchester and this radio channel changes. This is because multiple people are using the same channel.

Same here, so we divide the spectrum up into different channels. But like, there isn’t that many channels for WiFi as compared to radio.

Each station gets assigned a fixed frequency band

Unused transmission time in frequency bands go idle

6 station LAN - 1, 3, 4 have packets - frequency bands 2, 5,6 are idle.

1. What is a random access protocol? It’s basically what happens when you give someone a COMP219 exam. Nah just kidding.

When a node has packet to send, it:
* transmit at full channel datarateR
* No previous coordination among nodes
Two or more transmitting nodes results in a collision

Random Access MAC Protocol specifies:
* how to detect collisions
* How to recover from collisions

1.  What does CSMA stand for? Carrier sense multiple access. Basically, “listen before transmit”. If channel seems idle, transmit the entire frame. It it seems busy, defer transmission. 
2.  Can colliisions still occur in CSMA? Yes! Propagation delay means two nodes may not heareachothers transmission, so may collide. 
3.  In CSMA/CD what does CD stand for? “collision detection” 
4.  Do you use CSMA/CD for WiFi? No, not really. It’s quite difficult. 
5.  Explain how the CSMA/CD algorithm works: 

    * NIC receives datagram from network layer, creates frame
    * If NIC senses channel idle, starts frame transmission
    * If NIC senses channel busy, waits until channel idle then transmits
    * If NIC transmit entire frame without detecting another transmission, NIC is done with frame.
    * If NIC detects another transmission while transmitting, it aborts and sends raspberry jam (jk it’s called a jam signal)
    * After aborting NIc, enters binary (exponential) backoff:
    	* after nth collision, NIC chooses K at random from ${0, 1, 2, ..., 2^{m-1}}$
    	* Longer backoff interval with more collisions
    

1. What is polling? Master node invites slave nodes to transmit in turn, typically used with dumb slave devices.

Kinda sucks due to latency and a single point of failure.

1.  What is token passing? When you sit in a circle and pass the weed around with your friends. But the weed is a control token which lets people put things into it to send. And your friends are servers. And the circle doesn’t even have to be a circle it can be a square as long as it can go round lol. 
2.  With IPV4, how long is the address? 32 bits 
3.  With IPV6, how long is the address? 128 bits 
4.  What is a MAC address? An address burned into the NIC to identify it. 
5.  What is the MAC address used for? Used locally to get frame from one interface to anothere physically connected interface 
6.  How long is the MAC address? 48 bits (for most LANs) 
7.  Can a computer in India and a computer in the UK have the same MAC address? No, its unique per netwok adaptor. 
8.  What about IP address? Not at the same time, but it is possible. 
9.  Who administers the MAC addresses? IEEE 
10.  How do you determine a MAC address using the devices IP address? ARP table: each IP node on LAN has a table. IP/MAC address mappings for some lan nodes. 
11.  How does the ARP protocol work? A wants to send datagram to b B’s mac address not in A’s ARP table (becasue theyr’e sending it via lan and not via the internet you just need the MAC address) A broadcasts ARP query packet, containing Bs iP addresss 

    * dest MAC address = -ff-ff-ff-ff-ff-ff 
    the ff is a 2 digit hexadecimal number 
    * all nodes on LAN receive the arp query
    

B receives ARP packet, replies to a with its MAC address (replies with B’s mac address, if that sounded confusing)
Frame sent to A’s mac address (unicast)

A caches (saves) IP-to-MAC address pair in its ARP table until information becomes outdated (it times out, time out time set by whoever programs it)

Soft warte means the information times out (gets deleted) until that is refreshed

ARP is plug-and-play, so nodes create their ARP tables without intervention from a network administrator

1.  What is the dominant wired LAN technology? Ethernet 
2.  What is a bus network? You have one coaxial cable which runs through the room and acts as a bus. Whenever a computer sends something it places it onto this bus (coaxial cable) and sends it. 

This is super, super outdated

1. What is a star network? You have a network switch (in most instances it’s just a normal router. Also note that most normal modern day routers support Modulator / Demodulator (MODEM) technology so it can transform digital signals into analog signals (they travel further than digital, or they used to))

This network switch has laptops connected to it.

1.  What is an ethernet frame? When sending something via ethernet, the sender encapsulates the IP datagram into an ethernet frame. 
2.  How long is an ethernet frame address? 6 bytes 
3.  Is ethernet reliable? No. It’s connectionless, so no handshaking between sending and receiving NICs. 

It’s unreliable, receiving NIC doesn’t send ACK or NACKS

1.  What is Ethernet’s MAC protocol? Unslotted CSMA/CD with Binary (exponential) backoff 
2.  How does switch know A’ is reachable via interface 4, B’ is reachable by interface 5? Each switch has a switch table, each entry consists of the MAC address of host, and the interface to reach host, as well as the time stamp. 

“Looks like a routing table” Martin

1. How are entries created and maintained in a switch table? The switch learns which hosts can be reach through which interfaces.

When a frame is received, the switch learns the location of thre sender. It then records the sender / location pair in the switch table.

1. What is the difference between a switch and a router? Routers: network layer devices Switches: link-layer deivces

Both have forwarding tables.

Routers compute the tables using routing algorithms and IP addresses.

Switches learn the forwarding table using flood, learning, mac addresses

1. What are the main differences between wired and wireless technology? Lmao Martin doesn’t actually say this but one of them is WIRELESS. The other important things are:

WiFi has decreased signal strength (radio signal attenuates as it propagates through matter). Attenuate means “loses strength as it moves through things”

Interfence from other sources.

Multipath propagation: radio signal reflects off objects and ground, so can arrive at different times

Guided media is wires, where you guide it. Unguided media is WiFi where you just throw it out there.

1.  What is the MAC protocol of WiFi? CSMA/CA. Ethernet uses CSMA/C**D**. 
2.  How does CSMA/CA work in the WiFi protocol? 
3.  If sensed channel is idle for DIFS (a weird name for a time frame) then: transmit entire frame (no collision detection) 
4.  If sense channel is busy then: start random backoff time (exponential backoff/binary backoff) timer counts down while channel idle transmit when timer expires if no ACK, increase random backoff interval, repeat 2 
5.  Can we reserve an entire wireless channel? Yes! A device can send a request to reserve a channel to the base station (in wireless technology the base station is a fancy word for router). This is called an RTS (request to send) packet - it’s sent using CSMA. The base station broadcasts clear-to-send CTS response CTS is heard by all nodes. The sender transmits the frame, all other nodes defer transmissions. 
6.  Explain half duplex, full duplex and simplex. Simplex: Sending a signal without receiving anything back. Imagine a radio, you just receive a radio station you don’t request songs via the signal. 

Half duplex: you can send things back but only speaks a time. Like a human convo, you don’t talk over your friends when they’re speaking, you wait your turn.

Full duplex: fuck your friends, talk over them who cares???

1. What are the advantages and disadvantages of digital signals? Cheaper, less suspectible to noise, but greater attenuation.

The signal gets ‘smaller and smaller’ the longer it goes on for.

1.  What is signal attenuation? Signal strength falls off with distance. The received signal trength must be suffienclty higher than the noise to be received without error. 
2.  What is delay distortion? Occurs because the velocity of propagation of a signal through a medium varies with frequency. 
3.  In what medium does delay disortion occur? Only in guided medium 
4.  Is thermal a factor of noise within signals? Yes 
5.  What is intermodulation? Signals that are the sum and difference of original frequencies sharing a medium. 
6.  What is crosstalk? Call picked up during another talk 
7.  What is impulse? Electromagnetic interfence - usually from the sun. 
8.  When talking about the bandwidth of a channel, what do we measure it in? Cycles per second or Hertz 
9.  What is Nyquist bandwidth? Some guy said: 

    >If bandwidth is B, then highest signal transmission (baud) rate is 2B.
    

1.  What is the Nyquist bandwidth of something with bandwidth 3.1KHZ? 2B = 6100 bits It’s $max data rate = 2 * B * log2(M)$ 
2.  Suppose a voice channel (B = 3100 Hz) is used to transmit digital data via modem which uses 4 different signal states. What is the maximum data rate? $$2 * 3100 * 2bps = 12400 bps$$ 
3.  What is Shannon’s capactivty formula? Most communication channels have noise present. The amount of thermal noise present is measured by the ratio of signal power to noise power. This is called the signal-to-noise ration (S/N). 

Usually the ratio is not quoted, but this quantity:
$$10*log10(\frac{S}{N})$$
This is measured in decibels.

So S/N = 10 -> 10 decibels

A fixed analog voice telephone network is typically 30db.
251. What is Shannon’s law?
The maximum data rate of a noisy channel with bandwidth B and signal-to-noise ratio of S/N is:
$$Max data rate = B*log2(1+\frac{S}{N})$$

Let’s see an example.

The channel has bandwidth 3100hz
And signal-to-noise ratio of 30Db (S/N = 1000)

Max bits per second:
$$3100 log2(1 + 1000)$$
$$3100 log2(1001)$$
$$3100*9.9658 = 30,894 bps$$

1.  When do you use Nyquist / Shannon? Noise free, we use Nyquist Noisy channel we use Shannon. 
2.  Suppose the channel has a signal to noise ratio of 1023 , what is the maximum data rate of this channel with bandwidth 3000. Also, what is the maximum number of signal states M needed to achieve data rate of 2400 BPS? How many bits must each signal state encode? We use Shannon as Nyquist doesn’t talk about noise at all. Max data rate = $3000 * log2(1024)$ Something important to note: NO CALCULATORS in networking. He expects you to work out log2(1024) yourself. So this results in 10, so we do: $$3000 * 10 = 30,000 bps$$ To work out the second parts (how many bits must each signal state encode) we do: $$24,000 = 6000 * log2(M)$$ $$= 4 - log2(M)$$ $$= 16 = 2^4 = 2^{log2(m)}=M$$ 

254. What is twisted pair?
What we normally use for Ethernet. You have a pair of wires and you twist them.
255. What data can be transmitted in the physical layer?
Analog / digital
256. What does data represent?
He says analog represents video and digital represents hardware. I have literally no idea what this means, because data can represent anything lol.
257. Name and describe four different sources of noise?
Thermal (white noise)
Crosstalk
Intermodulation
Impulse such as lightning
258. What is the signal to noise ratio corresponding to 20dB?
$$10 * log10
259. Consider a communication channel with bandwidth B = 5000hz:
1. suppose S/N = 255, what is the maximum data rate of this channel?
2. What is the minimum number of signal states M needed to achieve a data rate of 20000 bps? How many states to encode?
TODO complete this

1. What is the name of a packet in each of the following layers?
2. Transport layer
3. Network layer
4. Link layer
5. Consider sending a 3400 byte datagram into a link that has an MTU of 500 bytes
6. Suppose an application generates  chunks of 160 bytes of data every 30msec and each chunk gets encapsulated in a TCP segment and then an IPv4 datagram. What percentage of each datagram will be application data?
7. Compute the CRC bits defined by the generator 1101 and the data bit string 11101 
