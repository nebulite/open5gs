ies.append({ "ie_type" : "IMSI", "ie_value" : "IMSI", "presence" : "C", "instance" : "0", "comment" : "The IMSI shall be included in the message on the S4/S11 interface, and on S5/S8 interface if provided by the MME/SGSN, except for the case:-	If the UE is emergency attached and the UE is UICCless.The IMSI shall be included in the message on the S4/S11 interface, and on S5/S8 interface if provided by the MME/SGSN, but not used as an identifierif UE is emergency attached but IMSI is not authenticated.The IMSI shall be included in the message on the S2a/S2b interface."})
ies.append({ "ie_type" : "MSISDN", "ie_value" : "MSISDN", "presence" : "C", "instance" : "0", "comment" : "For an E-UTRAN Initial Attach and a Handover from Trusted or Untrusted Non-3GPP IP Access to E-UTRAN the IE shall be included when used on the S11 interface, if provided in the subscription data from the HSS.For a PDP Context Activation procedure and a Handover from Trusted or Untrusted Non-3GPP IP Access to UTRAN/GERAN the IE shall be included when used on the S4 interface, if provided in the subscription data from the HSS. The IE shall be included for the case of a UE Requested PDN Connectivity, if the MME has it stored for that UE. It shall be included when used on the S5/S8 interfaces if provided by the MME/SGSN. The ePDG shall include this IE on the S2b interface during an Attach with GTP on S2b , UE initiated Connectivity to Additional PDN with GTP on S2b and a Handover to Untrusted Non-3GPP IP Access with GTP on S2b, Initial Attach for emergency session (GTP on S2b), if provided by the HSS/AAA. The TWAN shall include this IE on the S2a interface during an Initial Attach in WLAN on GTP S2a, UE initiated Connectivity to Additional PDN with GTP on S2a and a Handover to TWAN with GTP on S2a, if provided by the HSS/AAA."})
ies.append({ "ie_type" : "MEI", "ie_value" : "ME Identity", "presence" : "C", "instance" : "0", "comment" : "The MME/SGSN shall include the ME Identity (MEI) IE on the S11/S4 interface:-	If the UE is emergency attached and the UE is UICCless-	If the UE is emergency attached and the IMSI is not authenticatedFor all other cases the MME/SGSN shall include the ME Identity (MEI) IE on the S11/S4 interface if it is available."})
ies.append({ "ie_type" : "ULI", "ie_value" : "User Location Information", "presence" : "C", "instance" : "0", "comment" : "This IE shall be included on the S11 interface for E-UTRAN Initial Attach, a Handover from Trusted or Untrusted Non-3GPP IP Access to E-UTRAN and UE-requested PDN Connectivity procedures. It shall include ECGI and TAI. The MME/SGSN shall also include it on the S11/S4 interface for TAU/RAU/X2-Handover/Enhanced SRNS Relocation procedure if the PGW/PCRF has requested location information change reporting and MME/SGSN support location information change reporting."})
ies.append({ "ie_type" : "Serving Network", "ie_value" : "Serving Network", "presence" : "C", "instance" : "0", "comment" : "This IE shall be included on the S4/S11, S5/S8 and S2b interfaces for an E-UTRAN initial attach, a Handover from Trusted or Untrusted Non-3GPP IP Access to E-UTRAN, a PDP Context Activation, a Handover from Trusted or Untrusted Non-3GPP IP Access to UTRAN/GERAN, a UE requested PDN connectivity, an Attach with GTP on S2b, a UE initiated Connectivity to Additional PDN with GTP on S2b, a Handover to Untrusted Non-3GPP IP Access with GTP on S2b and an Initial Attach for emergency session (GTP on S2b). See NOTE 10."})
ies.append({ "ie_type" : "RAT Type", "ie_value" : "RAT Type", "presence" : "M", "instance" : "0", "comment" : "This IE shall be set to the 3GPP access type or to the value matching the characteristics of the non-3GPP access  the UE is using to attach to the EPS.The ePDG may use the access technology type of the untrusted non-3GPP access network if it is able to acquire it; otherwise it shall indicate Virtual as the RAT Type.The TWAN shall set the RAT Type value to WLAN on the S2a interface.See NOTE 3, NOTE 4."})
ies.append({ "ie_type" : "Indication", "ie_value" : "Indication Flags", "presence" : "C", "instance" : "0", "comment" : "This IE shall be included if any one of the applicable flags is set to 1.Applicable flags are:S5/S8 Protocol Type: This flag shall be set to 1 on the S11/S4 interfaces if the chosen protocol type for the S5/S8 interface is PMIP.Dual Address Bearer Flag: This flag shall be set to 1 on the S2b, S11/S4 and S5/S8 interfaces when the PDN Type, determined based on UE request and subscription record, is set to IPv4v6 and all SGSNs which the UE may be handed over to support dual addressing. This shall be determined based on node pre-configuration by the operator. (see also NOTE 5). The TWAN shall set this flag to 1 on the S2a interface if it supports IPv4 and IPv6 and the PDN Type determined from the UE request if single-connection mode or multi-connection mode is used (see 3GPPTS23.402[45]) and the user subscription data is set to IPv4v6.Handover Indication: This flag shall be set to 1 on the S11/S4 and S5/S8 interface during a Handover from Trusted or Untrusted Non-3GPP IP Access to E-UTRAN, or a Handover from Trusted or Untrusted Non-3GPP IP Access to UTRAN/GERAN procedures, or an Addition of a 3GPP access of NBIFOM procedure. This flag shall be set to 1 on the S2b interface during a Handover from 3GPP access to Untrusted Non-3GPP IP Access with GTP on S2b and IP address preservation is requested by the UE, or an Addition of an access using S2b of NBIFOM procedure. This flag shall be set to 1 on the S2a interface during a Handover from 3GPP access to TWAN with GTP on S2a and IP address preservation is requested by the UE, or an Addition of an access using S2a of NBIFOM procedure.Operation Indication: This flag shall be set to 1 on the S4/S11 interface for a TAU/RAU procedure with SGW relocation, Enhanced SRNS Relocation with SGW relocation, X2-based handovers with SGW relocation and MME triggered Serving GW relocation.Direct Tunnel Flag: This flag shall be set to 1 on the S4 interface if Direct Tunnel is used.Piggybacking Supported: This flag shall be set to 1 on the S11 interface only if the MME supports the piggybacking feature as described in Annex F of 3GPP TS 23.401 [3]. This flag shall be set to 1 on S5/S8 only if both the MME and the SGW support piggybacking.Change Reporting support Indication: This flag shall be set to 1 on S4/S11 and S5/S8 interfaces if the SGSN/MME supports location Info Change Reporting and if the SGSN/MMEs operator policy permits reporting of location change to the operator of the PGW with which the session is being established. See NOTE2. CSG Change Reporting Support Indication: This flag shall be set to 1 on S4/S11 and S5/S8 interfaces if the SGSN/MME supports CSG Information Change Reporting and if the SGSN/MMEs operator policy permits reporting of CSG Information change to the operator of the PGW with which the session is being established. See NOTE 2.Unauthenticated IMSI: This flag shall be set to 1 on the S4/S11 and S5/S8 interfaces if the IMSI present in the message is not authenticated and is for an emergency attached UE. PDN Pause Support Indication: this flag shall be set to 1 on the S5/S8 interface if the SGW supports the PGW Pause of Charging procedure. NBIFOM Support Indication: This flag shall be set to 1 on S11/S4 if the MME/SGSN supports NBIFOM.This flag shall be set to 1 on S5/S8 if both the SGW and the MME/SGSN support NBIFOM. This flag shall be set to 1 on S2a/S2b if the TWAN/ePDG supports NBIFOM. WLCP PDN Connection Modification Support Indication: This flag shall be set to 1 on the S2a interface if the TWAN supports the WLCP PDN Connection Modification procedure. UE Not Authorised Cause Code Support Indication: This flag shall be set to 1 on S4/S11 and S5/S8 interface if the SGSN/MME supports the UE not authorised by OCS or external AAA Server Cause Code. UE Available for Signalling Indication: this flag shall be set to 1 on S11/S4 during a TAU/RAU with SGW relocation procedure if there is pending network initiated PDN connection signalling for this PDN connection.  The SGW shall include this IE on S5/S8 if it receives the flag from the MME/SGSN. S11-U Tunnel Flag: this flag shall be set to 1 on the S11 interface if user data is transported in NAS signalling. Extended PCO Support Indication: this flag shall be set to 1 on S11 interface by the MME if the UE and the MME support ePCO; and this flag shall be set to 1 on S5/S8 interface by the SGW if the SGW supports ePCO and MME has set the flag to 1.Control Plane Only PDN Connection Indication: this flag shall be set to 1 over S11 and S5/S8 if the PDN Connection is set to Control Plane Only."})
ies.append({ "ie_type" : "F-TEID", "ie_value" : "Sender F-TEID for Control Plane", "presence" : "M", "instance" : "0", "comment" : ""})
ies.append({ "ie_type" : "F-TEID", "ie_value" : "PGW S5/S8 Address for Control Plane or PMIP", "presence" : "C", "instance" : "1", "comment" : "This IE shall be sent on the S11 / S4 interfaces. The TEID or GRE Key is set to 0 in the E-UTRAN initial attach, a Handover from Trusted or Untrusted Non-3GPP IP Access to E-UTRAN, the PDP Context Activation, a Handover from Trusted or Untrusted Non-3GPP IP Access to UTRAN/GERAN and the UE requested PDN connectivity procedures."})
ies.append({ "ie_type" : "APN", "ie_value" : "Access Point Name", "presence" : "M", "instance" : "0", "comment" : ""})
ies.append({ "ie_type" : "Selection Mode", "ie_value" : "Selection Mode", "presence" : "C", "instance" : "0", "comment" : "This IE shall be included on the S4/S11 and S5/S8 interfaces for an E-UTRAN initial attach, a Handover from Trusted or Untrusted Non-3GPP IP Access to E-UTRAN, a PDP Context Activation, a Handover from Trusted or Untrusted Non-3GPP IP Access to UTRAN/GERAN and a UE requested PDN connectivity. This IE shall be included on the S2b interface for an Initial Attach with GTP on S2b, a Handover to Untrusted Non-3GPP IP Access with GTP on S2b, a UE initiated Connectivity to Additional PDN with GTP on S2b and an Initial Attach for emergency session (GTP on S2b).It shall indicate whether a subscribed APN or a non subscribed APN chosen by the UE/MME/SGSN/ePDG/TWAN was selected, see NOTE 17.This IE shall be included on the S2a interface for an Initial Attach in WLAN on GTP S2a, a Handover to TWAN with GTP on S2a and a UE initiated Connectivity to Additional PDN with GTP on S2a. The value shall be set to MS or network provided APN, subscription verified."})
ies.append({ "ie_type" : "PDN Type", "ie_value" : "PDN Type", "presence" : "C", "instance" : "0", "comment" : "This IE shall be included on the S4/S11 and S5/S8 interfaces for an E-UTRAN initial attach, a Handover from Trusted or Untrusted Non-3GPP IP Access to E-UTRAN, a PDP Context Activation, a Handover from Trusted or Untrusted Non-3GPP IP Access to UTRAN/GERAN and a UE requested PDN connectivity.This IE shall be set to IPv4, IPv6, IPv4v6 or Non-IP. This is based on the UE request and the subscription record retrieved from the HSS (for MME see 3GPP TS 23.401 [3], clause 5.3.1.1, and for SGSN see 3GPP TS 23.060 [35], clause 9.2.1). See NOTE 1. See NOTE 14."})
ies.append({ "ie_type" : "PAA", "ie_value" : "PDN Address Allocation", "presence" : "C", "instance" : "0", "comment" : "This IE shall be included the S4/S11, S5/S8 and S2a/S2b interfaces for an E-UTRAN initial attach, a Handover from Trusted or Untrusted Non-3GPP IP Access to E-UTRAN, a PDP Context Activation, a Handover from Trusted or Untrusted Non-3GPP IP Access to UTRAN/GERAN, a UE requested PDN connectivity, an Attach with GTP on S2b, a UE initiated Connectivity to Additional PDN with GTP on S2b, a Handover to Untrusted Non-3GPP IP Access with GTP on S2b, an Initial Attach for emergency session (GTP on S2b, an Initial Attach in WLAN on GTP S2a, a UE initiated Connectivity to Additional PDN with GTP on S2a and a Handover to TWAN with GTP on S2a. For PMIP-based S5/S8, this IE shall also be included on the S4/S11 interfaces for TAU/RAU/Handover cases involving SGW relocation.The PDN type field in the PAA shall be set to IPv4, or IPv6 or IPv4v6, or Non-IP by MME, based on the UE request and the subscription record retrieved from the HSS (see subclause 8.12 and also NOTE 5).The TWAN shall set the PDN type field in the PAA to IPv4, or IPv6 or IPv4v6 based on the UE request if single-connection mode or multi-connection mode is used (see 3GPPTS23.402[45]), the IP versions the TWAN supports and the PDN type received in the user subscription data from the HSS/3GPP AAA Server.The ePDG shall set the PDN type field in the PAA to IPv4, or IPv6 or IPv4v6 based on the UE request and the subscription record retrieved from the HSS/3GPP AAA Server, or based on the UE request and the ePDG Emergency Configuration Data for an Initial Attach for emergency session (GTP on S2b).For static IP address assignment (for MME see 3GPP TS 23.401 [3], clause 5.3.1.1, for SGSN see 3GPP TS 23.060 [35], clause 9.2.1, for ePDG see 3GPP TS 23.402 [45] subclause 4.7.3, and for TWAN see 3GPP TS 23.402 [45] subclause 16.1.5), the MME/SGSN/ePDG/TWAN shall set the IPv4 address and/or IPv6 prefix length and IPv6 prefix and Interface Identifier based on the subscribed values received from HSS, if available. For PDN Type IPv4v6, either one of the IP versions (i.e. IPv4 address or IPv6 prefix and Interface Identifier) or both the IP versions may be statically provisioned in the HSS. If only one of the IP versions is statically provisioned in the HSS, the MME/SGSN/ePDG/TWAN shall set the other IP version as all zeros. The value of PDN Type field shall be consistent with the value of the PDN Type IE, if present in this message.For a Handover to Untrusted Non-3GPP IP Access with GTP on S2b, the ePDG shall set the IPv4 address and/or IPv6 prefix length and IPv6 prefix and Interface Identifier based on the IP address(es) received from the UE.For IP PDN connections, if static IP address assignment is not used (e.g. static address is not received from the HSS), and for scenarios other than a Handover to Untrusted Non-3GPP IP Access with GTP on S2b, the IPv4 address shall be set to 0.0.0.0, and/or the IPv6 Prefix Length and IPv6 prefix and Interface Identifier shall all be set to zero.For Non-IP PDN connections, the PDN Address and Prefix field shall not be present. See NOTE 14."})
ies.append({ "ie_type" : "APN Restriction", "ie_value" : "Maximum APN Restriction", "presence" : "C", "instance" : "0", "comment" : "This IE shall be included on the S4/S11 and S5/S8 interfaces in the E-UTRAN initial attach, a Handover from Trusted or Untrusted Non-3GPP IP Access to E-UTRAN, PDP Context Activation, a Handover from Trusted or Untrusted Non-3GPP IP Access to UTRAN/GERAN and UE Requested PDN connectivity procedures.This IE denotes the most stringent restriction as required by any already active bearer context. If there are no already active bearer contexts, this value is set to the least restrictive type."})
ies.append({ "ie_type" : "AMBR", "ie_value" : "Aggregate Maximum Bit Rate", "presence" : "C", "instance" : "0", "comment" : "This IE represents the APN-AMBR. It shall be included on the S4/S11, S5/S8 and S2a/S2b interfaces for an E-UTRAN initial attach, a Handover from Trusted or Untrusted Non-3GPP IP Access to E-UTRAN, UE requested PDN connectivity, PDP Context Activation procedure using S4, a Handover from Trusted or Untrusted Non-3GPP IP Access to UTRAN/GERAN, TAU/RAU/Handover from the Gn/Gp SGSN to the S4 SGSN/MME procedures, Attach with GTP on S2b, a Handover to Untrusted Non-3GPP IP Access with GTP on S2b, UE initiated Connectivity to Additional PDN with GTP on S2b, an Initial Attach for emergency session (GTP on S2b), Initial Attach in WLAN on GTP S2a, a Handover to TWAN with GTP on S2a and UE initiated Connectivity to Additional PDN with GTP on S2a."})
ies.append({ "ie_type" : "EBI", "ie_value" : "Linked EPS Bearer ID", "presence" : "C", "instance" : "0", "comment" : "This IE shall be included on S4/S11 in RAU/TAU/HO except in the Gn/Gp SGSN to MME/S4-SGSN RAU/TAU/HO procedures with SGW change to identify the default bearer of the PDN Connection"})
ies.append({ "ie_type" : "TWMI", "ie_value" : "Trusted WLAN Mode Indication", "presence" : "CO", "instance" : "0", "comment" : "The TWAN shall include this IE on S2a interface (during initial attach, handover to TWAN with GTP on S2a procedure, UE-initiated additional PDN connectivity procedures), if the single-connection mode or multiple-connection mode is used.The TWAN shall not include this IE if transparent single-connection mode is used. The PGW shall assume that transparent single-connection mode is used if it receives this message without this IE from the TWAN."})
ies.append({ "ie_type" : "PCO", "ie_value" : "Protocol Configuration Options", "presence" : "C", "instance" : "0", "comment" : "If MME/SGSN receives PCO from the UE during the Attach, PDN connectivity or Handover to 3GPP access procedures, the MME/SGSN shall forward the PCO IE to SGW. The SGW shall also forward it to PGW."})
ies.append({ "ie_type" : "Bearer Context", "ie_value" : "Bearer Contexts to be created", "presence" : "M", "instance" : "0", "comment" : "S Several IEs with the same type and instance value shall be included on the S4/S11 and S5/S8 interfaces as necessary to represent a list of Bearers. One single IE shall be included on the S2a/S2b interface.One bearer shall be included for E-UTRAN Initial Attach, PDP Context Activation, UE requested PDN Connectivity, Attach with GTP on S2b, UE initiated Connectivity to Additional PDN with GTP on S2b, Handovers between Untrusted Non-3GPP IP Access with GTP on S2b and 3GPP Access, Initial Attach for emergency session (GTP on S2b), Initial Attach in WLAN on GTP S2a, Handovers between TWAN with GTP on S2a and 3GPP Access and UE initiated Connectivity to Additional PDN with GTP on S2a.One or more bearers shall be included for a Handover/TAU/RAU with an SGW change. See NOTE 6 and NOTE 7."})
ies.append({ "ie_type" : "Bearer Context", "ie_value" : "Bearer Contexts to be removed", "presence" : "C", "instance" : "1", "comment" : "This IE shall be included on the S4/S11 interfaces for the TAU/RAU/Handover cases where any of the bearers existing before the TAU/RAU/Handover procedure will be deactivated as consequence of the TAU/RAU/Handover procedure.For each of those bearers, an IE with the same type and instance value shall be included.See NOTE 6 and NOTE 7."})
ies.append({ "ie_type" : "Trace Information", "ie_value" : "Trace Information", "presence" : "C", "instance" : "0", "comment" : "This IE shall be included on the S4/S11 interface if an SGW trace is activated, and/or on the S5/S8 and S2a/2b interfaces if a PGW trace is activated. See 3GPP TS 32.422 [18]."})
ies.append({ "ie_type" : "FQ-CSID", "ie_value" : "MME-FQ-CSID", "presence" : "C", "instance" : "0", "comment" : "This IE shall be included by the MME on the S11 interface and shall be forwarded by an SGW on the S5/S8 interfaces according to the requirements in 3GPP TS 23.007 [17]."})
ies.append({ "ie_type" : "FQ-CSID", "ie_value" : "SGW-FQ-CSID", "presence" : "C", "instance" : "1", "comment" : "This IE shall included by the SGW on the S5/S8 interfaces according to the requirements in 3GPP TS 23.007 [17]."})
ies.append({ "ie_type" : "FQ-CSID", "ie_value" : "ePDG-FQ-CSID", "presence" : "C", "instance" : "2", "comment" : "This IE shall be included by the ePDG on the S2b interface according to the requirements in 3GPP TS 23.007 [17]."})
ies.append({ "ie_type" : "FQ-CSID", "ie_value" : "TWAN-FQ-CSID", "presence" : "C", "instance" : "3", "comment" : "This IE shall be included by the TWAN on the S2a interface according to the requirements in 3GPP TS 23.007 [17]."})
ies.append({ "ie_type" : "UE Time Zone", "ie_value" : "UE Time Zone", "presence" : "CO", "instance" : "0", "comment" : "This IE shall be included by the MME over S11 during Initial Attach, a Handover from Trusted or Untrusted Non-3GPP IP Access to E-UTRAN and UE Requested PDN Connectivity procedure.This IE shall be included by the SGSN over S4 during PDP Context Activation procedure and a Handover from Trusted or Untrusted Non-3GPP IP Access to UTRAN/GERAN.This IE shall be included by the MME/SGSN over S11/S4 TAU/RAU/Handover with SGW relocation."})
ies.append({ "ie_type" : "UCI", "ie_value" : "User CSG Information", "presence" : "CO", "instance" : "0", "comment" : "This IE shall be included on the S4/S11 interface for E-UTRAN Initial Attach, a Handover from Trusted or Untrusted Non-3GPP IP Access to E-UTRAN, UE-requested PDN Connectivity, PDP Context Activation and a Handover from Trusted or Untrusted Non-3GPP IP Access to UTRAN using S4 procedures, if the UE is accessed via CSG cell or hybrid cell. The MME/SGSN shall also include it for TAU/RAU/Handover procedures with SGW relocation if the UE is accessed via a CSG cell or hybrid cell or leaves a CSG or hybrid cell and the PGW/PCRF has requested CSG info reporting and MME/SGSN support CSG info reporting. NOTE 11.The SGW shall include this IE on S5/S8 if it receives the User CSG information from MME/SGSN.See NOTE 10."})
ies.append({ "ie_type" : "Charging Characteristics", "ie_value" : "Charging Characteristics", "presence" : "C", "instance" : "0", "comment" : "This IE shall be included on the S4/S11, S5/S8 and S2a/S2b interfaces according to 3GPP TS 32.251 [8]"})
ies.append({ "ie_type" : "LDN", "ie_value" : "MME/S4-SGSN LDN", "presence" : "O", "instance" : "0", "comment" : "This IE is optionally sent by the MME to the SGW on the S11 interface and by the S4-SGSN to the SGW on the S4 interface (see 3GPP TS 32.423 [44]), when communicating the LDN to the peer node for the first time."})
ies.append({ "ie_type" : "LDN", "ie_value" : "SGW LDN", "presence" : "O", "instance" : "1", "comment" : "This IE is optionally sent by the SGW to the PGW on the S5/S8 interfaces (see 3GPP TS 32.423 [44]), when communicating the LDN to the peer node for the first time."})
ies.append({ "ie_type" : "LDN", "ie_value" : "ePDG LDN", "presence" : "O", "instance" : "2", "comment" : "This IE is optionally sent by the ePDG to the PGW on the S2b interfaces (see 3GPP TS 32.423 [44]), when contacting the peer node for the first time. "})
ies.append({ "ie_type" : "LDN", "ie_value" : "TWAN LDN", "presence" : "O", "instance" : "3", "comment" : "This IE may be sent by the TWAN to the PGW on the S2a interfaces (see 3GPP TS 32.423 [44]), when contacting the peer node for the first time. "})
ies.append({ "ie_type" : "Signalling Priority Indication", "ie_value" : "Signalling Priority Indication", "presence" : "CO", "instance" : "0", "comment" : "The SGSN/MME shall include this IE on the S4/S11 interface if the UE indicates low access priority when requesting to establish the PDN connection. The SGW shall forward this IE in the Create Session Request message on the S5/S8 interfaces if received from the MME/SGSN. "})
ies.append({ "ie_type" : "IP Address", "ie_value" : "UE Local IP Address", "presence" : "CO", "instance" : "0", "comment" : "The ePDG shall include this IE on the S2b interface during an Initial Attach for emergency session (GTP on S2b). Otherwise the ePDG shall include this IE on the S2b interface based on local policy. "})
ies.append({ "ie_type" : "Port Number", "ie_value" : "UE UDP Port", "presence" : "CO", "instance" : "0", "comment" : "The ePDG shall include this IE on the S2b interface if NAT is detected, the UDP encapsulation is used and the UE Local IP Address is present."})
ies.append({ "ie_type" : "APCO", "ie_value" : "Additional Protocol Configuration Options", "presence" : "CO", "instance" : "0", "comment" : "If multiple authentications are supported by the ePDG, the ePDG shall include this IE on the S2b interface and perform the corresponding procedures as specified for PAP and CHAP authentication of the UE with external networks in 3GPP TS 33.402 [50]."})
ies.append({ "ie_type" : "IP Address", "ie_value" : "HNB Local IP Address", "presence" : "CO", "instance" : "1", "comment" : "The MME/SGSN shall include this IE on S11/S4 interface if the MME/SGSN receives this information from H(e)NB in UE associated S1/Iu signalling according (see 3GPP TS 23.139 [51]) during:  E-UTRAN Initial Attach, a Handover from Trusted or Untrusted Non-3GPP IP Access to E-UTRAN, UE-requested PDN Connectivity, PDP Context Activation and a a Handover from Trusted or Untrusted Non-3GPP IP Access to UTRAN using S4;TAU/RAU/X2-based handover/Enhanced Serving RNS Relocation Procedure with SGW change, if the PGW/PCRF has requested H(e)NB information reporting for the PDN connection.The SGW shall forward this IE on S5/S8 interface if the SGW receives it from the MME/SGSN."})
ies.append({ "ie_type" : "Port Number", "ie_value" : "HNB UDP Port", "presence" : "CO", "instance" : "1", "comment" : "The MME/SGSN shall include this IE on S11/S4 interface if the MME/SGSN receives this information from H(e)NB in UE associated S1/Iu signalling according (see 3GPP TS 23.139 [51]) during:  E-UTRAN Initial Attach, a Handover from Trusted or Untrusted Non-3GPP IP Access to E-UTRAN, UE-requested PDN Connectivity, PDP Context Activation and a Handover from Trusted or Untrusted Non-3GPP IP Access to UTRAN using S4;TAU/RAU/X2-based handover/Enhanced Serving RNS Relocation Procedure with SGW relocation, if the PGW/PCRF has requested H(e)NB information reporting for the PDN connection.The SGW shall forward this IE on S5/S8 interface if the SGW receives it from the MME/SGSN."})
ies.append({ "ie_type" : "IP Address", "ie_value" : "MME/S4-SGSN Identifier", "presence" : "CO", "instance" : "2", "comment" : "If the PGW triggered SGW restoration procedure is supported, the MME/S4-SGSN shall include this IE on S11/S4 interface and the SGW shall forward this IE on S5 interface in the existing signalling as specified in 3GPP TS 23.007 [17].If the overload control feature is supported by the MME/S4-SGSN and is activated for the PLMN to which the PGW belongs (see subclause 12.3.11), the MME/S4-SGSN shall include this IE on the S11/S4 interface. In that case, the SGW shall forward this IE on the S5/S8 interface."})
ies.append({ "ie_type" : "TWAN Identifier", "ie_value" : "TWAN Identifier", "presence" : "CO", "instance" : "0", "comment" : "This IE shall be included on the S2a interface for Initial Attach in WLAN procedure, UE-initiated Connectivity to Additional PDN with GTP on S2a and handover to TWAN with GTP on S2a procedure as specified in 3GPP TS 23.402 [45]. "})
ies.append({ "ie_type" : "IP Address", "ie_value" : "ePDG IP Address", "presence" : "O", "instance" : "3", "comment" : "This IE may be included on the S2b interface based on local policy for Fixed Broadband access network interworking, see 3GPPTS23.139[51]. If present, it shall contain the ePDG IP address which is used as IKEv2 tunnel endpoint with the UE."})
ies.append({ "ie_type" : "CN Operator Selection Entity", "ie_value" : "CN Operator Selection Entity", "presence" : "CO", "instance" : "0", "comment" : "In shared networks, the SGSN shall include this IE on the S4 interface for a PDP Context Activation, a Handover from Trusted or Untrusted Non-3GPP IP Access to UTRAN/GERAN and RAU with SGW relocation procedures, if the information is available,  to indicate whether the Serving Network has been selected by the UE or by the network."})
ies.append({ "ie_type" : "Presence Reporting Area Information", "ie_value" : "Presence Reporting Area Information", "presence" : "CO", "instance" : "0", "comment" : "The MME/SGSN shall include this IE in the following procedures, if the PGW/PCRF requested reporting changes of UE presence in a Presence Reporting Area and the MME/SGSN supports such reporting:-	TAU/RAU/Handover procedures with SGW relocation and MME/SGSN change. The new MME/SGSN shall then indicate whether the UE is inside or outside the Presence Reporting Area; -	TAU/RAU/Handover procedures with SGW relocation and without MME/SGSN change, if the UE enters or leaves the Presence Reporting Area."})
ies.append({ "ie_type" : "Overload Control Information", "ie_value" : "MME/S4-SGSN's Overload Control Information", "presence" : "O", "instance" : "0", "comment" : "During an overload condition, the MME/S4-SGSN may include this IE on the S11/S4 interface if the overload control feature is supported by the MME/S4-SGSN and is activated for the PLMN to which the PGW belongs (see clause 12.3.11).When present, the MME/S4-SGSN shall provide only one instance of this IE, representing its overload information."})
ies.append({ "ie_type" : "Overload Control Information", "ie_value" : "SGW's Overload Control Information", "presence" : "O", "instance" : "1", "comment" : "During an overload condition, the SGW may include this IE over the S5/S8 interface if the overload control feature is supported by the SGW and is activated for the PLMN to which the PGW belongs (see clause 12.3.11).When present, the SGW shall provide only one instance of this IE, representing its overload information."})
ies.append({ "ie_type" : "Overload Control Information", "ie_value" : "TWAN/ePDG's Overload Control Information", "presence" : "O", "instance" : "2", "comment" : "During an overload condition, the TWAN/ePDG may include this IE over the S2a/S2b interface if the overload control feature is supported by the TWAN/ePDG and is activated for the PLMN to which the PGW belongs (see clause 12.3.11).When present, the TWAN/ePDG shall provide only one instance of this IE, representing its overload information."})
ies.append({ "ie_type" : "Millisecond Time Stamp", "ie_value" : "Origination Time Stamp", "presence" : "CO", "instance" : "0", "comment" : "The MME/SGSN and the TWAN/ePDG shall include this IE on the S11/S4 and S2a/S2b interface respectively, in the conditions specified in subclause 13.2.When present, the Origination Time Stamp shall contain the UTC time when the originating entity initiated the request."})
ies.append({ "ie_type" : "Integer Number", "ie_value" : "Maximum Wait Time", "presence" : "CO", "instance" : "0", "comment" : "The MME/SGSN and the TWAN/ePDG shall include this IE on the S11/S4 and S2a/S2b interface respectively, in the conditions specified in subclause 13.3.When present, the Maximum Wait Time shall contain the duration (number of milliseconds since the Origination Time Stamp) during which the originator of the request waits for a response."})
ies.append({ "ie_type" : "TWAN Identifier", "ie_value" : "WLAN Location Information", "presence" : "CO", "instance" : "1", "comment" : "This IE shall be included on the S2b interface if the WLAN Location Information is available. "})
ies.append({ "ie_type" : "TWAN Identifier Timestamp", "ie_value" : "WLAN Location Timestamp", "presence" : "CO", "instance" : "0", "comment" : "This IE shall be included on the S2b interface, if the WLAN Location Timestamp is available. "})
ies.append({ "ie_type" : "F-Container", "ie_value" : "NBIFOM Container", "presence" : "CO", "instance" : "0", "comment" : "This IE shall be included on the S11/S4 or S2a/S2b interfaces if the MME/S4-SGSN or the TWAN/ePDG receives an NBIFOM Container from the UE as specified in TS 24.161 73]. The Container Type shall be set to 4."})
ies.append({ "ie_type" : "Remote UE Context", "ie_value" : "Remote UE Context Connected", "presence" : "CO", "instance" : "0", "comment" : "The MME shall include this IE on the S11 interface during a SGW relocation procedure if such information is available. Several IEs with the same type and instance value may be included as necessary to represent a list of remote UEs connected."})
ies.append({ "ie_type" : "Node Identifier", "ie_value" : "3GPP AAA Server Identifier", "presence" : "O", "instance" : "0", "comment" : "The ePDG/TWAN may include this IE on the S2a/S2b interface to provide the selected 3GPP AAA server identifier to the PGW. See NOTE 13."})
ies.append({ "ie_type" : "ePCO", "ie_value" : "Extended Protocol Configuration Options", "presence" : "CO", "instance" : "0", "comment" : "If the MME receives ePCO from the UE during the Initial Attach, UE requested PDN Connectivity procedures, the MME shall forward the ePCO IE to the SGW if the MME supports ePCO. The SGW shall also forward it to the PGW if the SGW supports ePCO. See NOTE 15."})
ies.append({ "ie_type" : "Serving PLMN Rate Control", "ie_value" : "Serving PLMN Rate Control", "presence" : "CO", "instance" : "0", "comment" : "The MME shall include this IE on the S11 interface if  Serving PLMN Rate control is configured by the MME operator and the PDN Connection is set to Control Plane Only:-	during an Initial Attach, or a UE Requested PDN Connectivity procedure.-	during an inter MME TAU with SGW relocation procedureSee NOTE 18.The SGW shall include this IE on S5/S8 if it receives this IE from MME.  "})
ies.append({ "ie_type" : "Counter", "ie_value" : "MO Exception Data Counter", "presence" : "CO", "instance" : "0", "comment" : "The MME shall include the counter if it has received the counter for RRC cause MO Exception data in the Context Response message during a TAU with an MME and SGW change."})
ies.append({ "ie_type" : "Port Number", "ie_value" : "UE TCP Port", "presence" : "CO", "instance" : "2", "comment" : "The ePDG shall include this IE on the S2b interface if NAT is detected, the TCP encapsulation is used and the UE Local IP Address is present."})
msg_list[key]["ies"] = ies
