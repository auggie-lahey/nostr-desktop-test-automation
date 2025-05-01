Nostrability POC	

Clients - Nostrudel, Coracle, Iris

Tools - selenium, nostrcli (nak?)

Relay - ? same for all notes (public - migration to standalone after POC maybe for relay testing in future)

Test Suite 0 (Nip-10)
	Test Case 0 - view of kind 1 is correct
• 	create kind 1 (via nak)
• 		verify that it looks normal on clients
• 	create threaded response
• 		verify that it looks normal on clients 
• 	https://damus.io/nevent1qqsw2eycsc7ehgvu83unpxs7aqedukhtjjzvvx0ptfpde656r7k3jqcpz4mhxue69uhhyetvv9ujumt0wd68ytnsw43qzenhwden5te0ve5kcar9wghxummnw3ezuamfdejj7mnsw43rz7tpw4krs6esx5unxdehw5ukcum4xcmkgefh0ymrxdmhx348gem9w4mkxmtgx4hrwdec8pkrv7rwd3h8yemnxd68v6ndvclkyun0v9jxxctnws7hgun4v5q3vamnwvaz7tmjv4kxz7fwdehhxarj9e3xzmnyqyt8wumn8ghj7un9d3shjtnswf5k6ctv9ehx2aq7s4tqx
	Test Case 1 - creation of kind 1 is correct



Modifications: 
• Tests with out-of-deprecated-order markers for those over-relying on deprecated form
• Tests with a single reply marker, interpreted as reply-to-root: {root: id_a, reply_id: id_a}
• Tests with a single root marker and no mentions or replys (what is this interepreted as? reply-to-root?)

Bonus: 
• do the same thing but don't use the CLI at all
• ie nostrudel to Coracle, Iris

Bonus++: 
• same thing but as a matrix of cases. 

Output: 
spreadsheet of test cases and pass fail

Future posibilities: 
Doing this with mobile clients
doing this with more desktop clients
using DVM for running tests against your client. 
Automatic test case matrix generation


