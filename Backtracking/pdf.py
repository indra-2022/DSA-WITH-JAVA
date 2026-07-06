from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import cm
from reportlab.lib import colors
from reportlab.platypus import (
    SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle,
    HRFlowable, PageBreak, KeepTogether
)
from reportlab.lib.enums import TA_CENTER, TA_LEFT, TA_JUSTIFY
from reportlab.platypus import Flowable

WIDTH, HEIGHT = A4

# ── Colour Palette ───────────────────────────────────────────────────────
TEAL         = colors.HexColor("#1D9E75")
PURPLE       = colors.HexColor("#7F77DD")
AMBER        = colors.HexColor("#D8A030")
RED          = colors.HexColor("#E24B4A")
BLUE         = colors.HexColor("#2D7DD2")
DARK         = colors.HexColor("#1A1A2E")
MID_GRAY     = colors.HexColor("#555555")
LIGHT_BG     = colors.HexColor("#F4F6F9")
TEAL_LIGHT   = colors.HexColor("#E8F7F2")
PURPLE_LIGHT = colors.HexColor("#F0EFFC")
AMBER_LIGHT  = colors.HexColor("#FDF5E6")
RED_LIGHT    = colors.HexColor("#FDF0F0")
BLUE_LIGHT   = colors.HexColor("#EAF3FD")
BORDER_GRAY  = colors.HexColor("#CCCCCC")

# ── Styles ────────────────────────────────────────────────────────────────
def S(name, **kw):
    return ParagraphStyle(name, **kw)

ch_title  = S("ChTitle", fontSize=20, textColor=TEAL,    fontName="Helvetica-Bold",
               spaceBefore=18, spaceAfter=6, leading=26)
sec_title = S("SecTitle", fontSize=13, textColor=DARK,   fontName="Helvetica-Bold",
               spaceBefore=10, spaceAfter=4, leading=18)
body      = S("Body",     fontSize=10, textColor=DARK,   fontName="Helvetica",
               leading=15, spaceAfter=4, alignment=TA_JUSTIFY)
bullet_s  = S("Bullet",  fontSize=10, textColor=DARK,   fontName="Helvetica",
               leading=15, leftIndent=16, spaceAfter=3, bulletIndent=6)
note_s    = S("Note",    fontSize=9.5, textColor=MID_GRAY, fontName="Helvetica-Oblique",
               leading=14, spaceAfter=4)
formula_s = S("Formula", fontSize=10, textColor=PURPLE, fontName="Helvetica-Bold",
               leading=14, spaceAfter=4, alignment=TA_CENTER,
               backColor=PURPLE_LIGHT, leftIndent=20, rightIndent=20)
toc_s     = S("TOC",     fontSize=11, textColor=DARK,   fontName="Helvetica",
               leading=22, leftIndent=10)
tag_s     = S("Tag",     fontSize=9,  textColor=MID_GRAY, fontName="Helvetica",
               leading=13, leftIndent=26, spaceAfter=2)

# ── Helpers ───────────────────────────────────────────────────────────────
def HR(color=TEAL, thickness=1.2):
    return HRFlowable(width="100%", thickness=thickness, color=color, spaceAfter=6)

def SP(h=6):   return Spacer(1, h)
def B(text):   return Paragraph(f"• {text}", bullet_s)
def P(text):   return Paragraph(text, body)
def SEC(text): return Paragraph(text, sec_title)
def NOTE(text):return Paragraph(f"<i>Real-world analogy: {text}</i>", note_s)
def TAG(text): return Paragraph(f"    ↳ {text}", tag_s)
def FMT(text): return Paragraph(text, formula_s)

# ── Custom Flowables ──────────────────────────────────────────────────────
class ColorBox(Flowable):
    def __init__(self, title, items, bg, border):
        Flowable.__init__(self)
        self.title = title; self.items = items
        self.bg = bg; self.border = border

    def wrap(self, aw, ah):
        self._w = aw
        self.height = 28 + 15 * len(self.items) + 14
        return (aw, self.height)

    def draw(self):
        c = self.canv
        w, h = self._w, self.height
        c.setFillColor(self.bg)
        c.roundRect(0, 0, w, h, 6, fill=1, stroke=0)
        c.setStrokeColor(self.border); c.setLineWidth(1.2)
        c.roundRect(0, 0, w, h, 6, fill=0, stroke=1)
        c.setFillColor(self.border)
        c.roundRect(0, h-26, w, 26, 6, fill=1, stroke=0)
        c.setFillColor(colors.white); c.setFont("Helvetica-Bold", 11)
        c.drawString(10, h-18, self.title)
        c.setFillColor(DARK); c.setFont("Helvetica", 9.5)
        y = h - 42
        for item in self.items:
            c.drawString(12, y, f"• {item}"); y -= 15


class StepBox(Flowable):
    """Numbered step boxes in a row."""
    def __init__(self, steps, color):
        Flowable.__init__(self)
        self.steps = steps; self.color = color

    def wrap(self, aw, ah):
        self._w = aw
        self.height = 70
        return (aw, self.height)

    def draw(self):
        c = self.canv
        n = len(self.steps)
        w = self._w
        box_w = (w - (n-1)*6) / n
        for i, (title, desc) in enumerate(self.steps):
            x = i * (box_w + 6)
            c.setFillColor(self.color)
            c.roundRect(x, 0, box_w, 68, 5, fill=1, stroke=0)
            c.setFillColor(colors.white)
            c.setFont("Helvetica-Bold", 18)
            c.drawCentredString(x + box_w/2, 44, str(i+1))
            c.setFont("Helvetica-Bold", 8)
            c.drawCentredString(x + box_w/2, 28, title)
            c.setFont("Helvetica", 7.5)
            # wrap desc
            words = desc.split()
            lines = []; cur = ""
            for w2 in words:
                if len(cur) + len(w2) + 1 < 22: cur += (" " if cur else "") + w2
                else: lines.append(cur); cur = w2
            if cur: lines.append(cur)
            y2 = 18
            for ln in lines[:2]:
                c.drawCentredString(x + box_w/2, y2, ln); y2 -= 10


class ArrowStep(Flowable):
    """Two-column box with arrow in between for comparison."""
    def __init__(self, left_title, left_items, right_title, right_items,
                 left_color, right_color):
        Flowable.__init__(self)
        self.lt=left_title; self.li=left_items
        self.rt=right_title; self.ri=right_items
        self.lc=left_color; self.rc=right_color

    def wrap(self, aw, ah):
        self._w = aw
        rows = max(len(self.li), len(self.ri))
        self.height = 30 + 15*rows + 14
        return (aw, self.height)

    def draw(self):
        c = self.canv; w = self._w; h = self.height
        hw = (w - 30) / 2
        for x, title, items, col in [
            (0, self.lt, self.li, self.lc),
            (hw+30, self.rt, self.ri, self.rc),
        ]:
            bg = colors.HexColor("#E8F7F2") if col==TEAL else colors.HexColor("#FDF0F0")
            c.setFillColor(bg)
            c.roundRect(x, 0, hw, h, 6, fill=1, stroke=0)
            c.setStrokeColor(col); c.setLineWidth(1)
            c.roundRect(x, 0, hw, h, 6, fill=0, stroke=1)
            c.setFillColor(col)
            c.roundRect(x, h-24, hw, 24, 6, fill=1, stroke=0)
            c.setFillColor(colors.white); c.setFont("Helvetica-Bold", 10)
            c.drawCentredString(x+hw/2, h-16, title)
            c.setFillColor(DARK); c.setFont("Helvetica", 9)
            y = h-40
            for item in items:
                c.drawString(x+8, y, f"• {item}"); y -= 15
        # arrow
        ax = hw + 5; ay = h/2
        c.setStrokeColor(MID_GRAY); c.setLineWidth(1.5)
        c.line(ax, ay, ax+20, ay)
        c.setFillColor(MID_GRAY)
        c.polygon([ax+20, ay, ax+14, ay+4, ax+14, ay-4], fill=1, stroke=0)


class CoverPage(Flowable):
    def wrap(self, aw, ah): return aw, ah
    def draw(self):
        c = self.canv; w = WIDTH; h = HEIGHT
        c.setFillColor(DARK); c.rect(0, 0, w, h, fill=1, stroke=0)
        c.setFillColor(colors.HexColor("#0D3B66"))
        c.rect(0, h*0.32, w, h*0.68, fill=1, stroke=0)
        c.setFillColor(TEAL); c.rect(0, h*0.32-3, w, 6, fill=1, stroke=0)
        # title
        c.setFillColor(colors.white); c.setFont("Helvetica-Bold", 34)
        c.drawCentredString(w/2, h*0.63, "Computer Networks")
        c.setFont("Helvetica-Bold", 20)
        c.setFillColor(colors.HexColor("#7FD8BD"))
        c.drawCentredString(w/2, h*0.575, "Transport, Application & Emerging Concepts")
        c.setStrokeColor(TEAL); c.setLineWidth(2)
        c.line(w*0.15, h*0.545, w*0.85, h*0.545)
        # chapter tags
        c.setFillColor(colors.HexColor("#BBDDFF")); c.setFont("Helvetica", 12)
        for i, t in enumerate([
            "Ch 5: Transport Layer — TCP, UDP, Port Addressing, Congestion Control",
            "Ch 6: Application Layer — DNS, HTTP, FTP, SMTP, POP3, IMAP, SSH",
            "Ch 7: Emerging Concepts — Cloud, IoT, MQTT, CoAP, SDN",
        ]):
            c.drawCentredString(w/2, h*0.50 - i*20, t)
        # info box
        c.setFillColor(colors.HexColor("#1A3550"))
        c.roundRect(w*0.15, h*0.14, w*0.70, 110, 10, fill=1, stroke=0)
        c.setStrokeColor(TEAL); c.setLineWidth(1.5)
        c.roundRect(w*0.15, h*0.14, w*0.70, 110, 10, fill=0, stroke=1)
        c.setFillColor(colors.white); c.setFont("Helvetica-Bold", 13)
        c.drawCentredString(w/2, h*0.14+88, "Indranil Ganguly")
        c.setFillColor(colors.HexColor("#BBDDFF")); c.setFont("Helvetica", 10)
        for i, ln in enumerate([
            "Subject: Computer Networks  |  Semester Exam Revision",
            "Easy Language + Real-World Analogies",
            "Prepared with Claude AI",
        ]):
            c.drawCentredString(w/2, h*0.14+62 - i*20, ln)
        c.setFillColor(colors.HexColor("#7FD8BD")); c.setFont("Helvetica", 9)
        c.drawCentredString(w/2, 28, "Computer Networks Study Guide  |  Chapters 5, 6 & 7")


# ── Document ──────────────────────────────────────────────────────────────
doc = SimpleDocTemplate(
    "/mnt/user-data/outputs/Transport_App_Emerging_Notes.pdf",
    pagesize=A4,
    leftMargin=2*cm, rightMargin=2*cm,
    topMargin=2*cm,  bottomMargin=2*cm,
    title="Transport, Application & Emerging Networking Notes",
    author="Indranil Ganguly",
)
story = []

# ═══════════════════════════════════════════════════════════
# COVER
# ═══════════════════════════════════════════════════════════
story.append(CoverPage())
story.append(PageBreak())

# ═══════════════════════════════════════════════════════════
# TABLE OF CONTENTS
# ═══════════════════════════════════════════════════════════
story.append(Paragraph("Table of Contents", ch_title))
story.append(HR())
story.append(SP(4))
toc = [
    ("CHAPTER 5", "TRANSPORT LAYER", ""),
    ("5.1", "What is the Transport Layer?", ""),
    ("5.2", "Functions of the Transport Layer", ""),
    ("5.3", "TCP — Transmission Control Protocol", ""),
    ("5.4", "TCP 3-Way Handshake (Connection Setup)", ""),
    ("5.5", "TCP 4-Way Handshake (Connection Teardown)", ""),
    ("5.6", "UDP — User Datagram Protocol", ""),
    ("5.7", "TCP vs UDP Comparison", ""),
    ("5.8", "Port Addressing", ""),
    ("5.9", "Congestion Control — Leaky Bucket", ""),
    ("5.10","Congestion Control — Token Bucket", ""),
    ("CHAPTER 6", "APPLICATION LAYER PROTOCOLS", ""),
    ("6.1", "DNS — Domain Name System", ""),
    ("6.2", "HTTP & HTTPS", ""),
    ("6.3", "FTP — File Transfer Protocol", ""),
    ("6.4", "Email Protocols: SMTP, POP3, IMAP", ""),
    ("6.5", "Remote Login: Telnet & SSH", ""),
    ("6.6", "File Sharing: NFS & SMB", ""),
    ("6.7", "SNMP — Simple Network Management Protocol", ""),
    ("CHAPTER 7", "EMERGING NETWORKING CONCEPTS", ""),
    ("7.1", "Cloud Networking Basics", ""),
    ("7.2", "Internet of Things (IoT)", ""),
    ("7.3", "MQTT Protocol", ""),
    ("7.4", "CoAP Protocol", ""),
    ("7.5", "Software-Defined Networking (SDN)", ""),
    ("—",   "Quick Revision Summary", ""),
]
for num, title, _ in toc:
    if num in ("CHAPTER 5","CHAPTER 6","CHAPTER 7"):
        story.append(SP(6))
        story.append(Paragraph(f"<b>{num}: {title}</b>", ParagraphStyle(
            "TocCh", fontSize=12, textColor=TEAL, fontName="Helvetica-Bold", leading=20)))
    else:
        story.append(Paragraph(f"<b>{num}</b>  {title}", toc_s))
story.append(PageBreak())


# ═══════════════════════════════════════════════════════════
# CHAPTER 5 — TRANSPORT LAYER
# ═══════════════════════════════════════════════════════════
story.append(Paragraph("Chapter 5: Transport Layer", ch_title))
story.append(HR())
story.append(SP(4))

# 5.1 What is Transport Layer
story.append(SEC("5.1  What is the Transport Layer?"))
story.append(P(
    "The <b>Transport Layer</b> is Layer 4 of the OSI model. It sits between the "
    "Application Layer (above) and the Network Layer (below). While the Network Layer "
    "delivers packets from computer to computer, the Transport Layer delivers data "
    "from <b>application to application</b> — process to process."
))
story.append(SP(4))
story.append(NOTE(
    "Think of the Network Layer as the post office delivering a parcel to a building. "
    "The Transport Layer is the building's receptionist who figures out which flat "
    "(which application) the parcel belongs to, and hands it to the right person."
))
story.append(SP(6))

story.append(ColorBox("The Big Picture", [
    "Network Layer delivers packet: Computer A  -->  Computer B",
    "Transport Layer delivers data: Chrome browser  -->  Web server (process-to-process)",
    "Two main protocols: TCP (reliable, ordered) and UDP (fast, no guarantees)",
    "Uses PORT NUMBERS to identify which application should receive the data",
], TEAL_LIGHT, TEAL))
story.append(SP(10))

# 5.2 Functions
story.append(SEC("5.2  Functions of the Transport Layer"))
funcs = [
    ("Process-to-Process Delivery",
     "Network Layer gets data to the right computer. Transport Layer then gets it "
     "to the right APPLICATION running on that computer using port numbers. "
     "Example: Port 80 = web browser, Port 25 = email."),
    ("Segmentation & Reassembly",
     "Big data files are too large to send in one go. The Transport Layer breaks "
     "them into smaller pieces called SEGMENTS. At the other end, it reassembles "
     "them in the correct order. Like tearing a long letter into pages, mailing "
     "each page separately, then re-reading them in order."),
    ("Connection Management",
     "TCP establishes a connection before sending data (3-way handshake) and "
     "closes it properly after (4-way handshake). Like calling someone before "
     "sending a long fax: 'Are you ready?' — 'Yes, ready.' — 'Sending now.'"),
    ("Flow Control",
     "The sender should not send data faster than the receiver can process. "
     "Like a teacher speaking slowly so students can take notes — Transport Layer "
     "tells the sender to slow down if the receiver's buffer is full."),
    ("Error Control",
     "Ensures data arrives correctly. Uses checksums to detect errors. If a "
     "segment is lost or corrupted, it requests retransmission. Like asking "
     "'Sorry, could you repeat that?' in a noisy phone call."),
    ("Congestion Control",
     "If the network is overloaded (too much traffic), the Transport Layer slows "
     "down the sender to reduce congestion. Like cars slowing down near a toll "
     "booth to avoid gridlock."),
    ("Multiplexing & Demultiplexing",
     "Multiplexing: Multiple applications (Chrome, Skype, WhatsApp) can send data "
     "simultaneously using the same network connection — each using different ports. "
     "Demultiplexing: At receiver, Transport Layer reads port number and delivers "
     "each segment to the correct application."),
]
for title, desc in funcs:
    story.append(KeepTogether([
        Paragraph(f"<b>{title}</b>", bullet_s),
        Paragraph(f"    {desc}", tag_s),
        SP(4),
    ]))
story.append(PageBreak())

# 5.3 TCP
story.append(SEC("5.3  TCP — Transmission Control Protocol"))
story.append(P(
    "<b>TCP</b> is a <b>connection-oriented, reliable</b> protocol. It guarantees that "
    "every byte of data arrives at the destination, in the correct order, without errors. "
    "It is used whenever accuracy is more important than speed."
))
story.append(NOTE(
    "TCP is like sending a registered post parcel. You get an acknowledgement when it "
    "reaches the destination. If the parcel is lost, the courier re-sends it. Slower "
    "than ordinary post, but guaranteed delivery."
))
story.append(SP(6))
for item in [
    "Connection-oriented: Must establish a connection before sending any data",
    "Reliable: Every segment is acknowledged (ACK). Lost segments are retransmitted",
    "Ordered delivery: Segments are numbered; receiver reorders if they arrive out-of-order",
    "Flow control: Uses sliding window to avoid overwhelming the receiver",
    "Congestion control: Slows down if network is congested (Slow Start, Congestion Avoidance)",
    "Full duplex: Both sides can send and receive simultaneously",
    "Used for: Web browsing (HTTP/HTTPS), Email (SMTP), File transfer (FTP), SSH",
]:
    story.append(B(item))
story.append(SP(10))

# 5.4 3-Way Handshake
story.append(SEC("5.4  TCP 3-Way Handshake — How a Connection is ESTABLISHED"))
story.append(P(
    "Before TCP sends any data, it must first establish a connection between client "
    "and server using a 3-step process called the <b>3-Way Handshake</b>."
))
story.append(NOTE(
    "Imagine you call a friend: (1) You: 'Hello, can you hear me?' — (2) Friend: "
    "'Yes I can hear you, can you hear me?' — (3) You: 'Yes!' Now both sides know "
    "the line is working. That's the 3-way handshake!"
))
story.append(SP(6))

story.append(StepBox([
    ("SYN",      "Client sends SYN (synchronise). 'I want to connect! My seq=100'"),
    ("SYN-ACK",  "Server replies SYN-ACK. 'OK! My seq=200, ACK=101'"),
    ("ACK",      "Client sends ACK. 'Got it! ACK=201. Connection open!'"),
], TEAL))
story.append(SP(8))

hw3 = [
    ["Step", "Who Sends", "Message",      "What it Means"],
    ["1",    "Client→Server", "SYN",      "I want to connect. My starting sequence number is X"],
    ["2",    "Server→Client", "SYN + ACK","OK! I'm ready (seq=Y). I got your seq (ack=X+1)"],
    ["3",    "Client→Server", "ACK",      "Great! Got your seq (ack=Y+1). Connection open now!"],
]
t = Table(hw3, colWidths=[1.5*cm, 3.5*cm, 3.5*cm, 8*cm])
t.setStyle(TableStyle([
    ('BACKGROUND', (0,0),(-1,0), TEAL),
    ('TEXTCOLOR',  (0,0),(-1,0), colors.white),
    ('FONTNAME',   (0,0),(-1,0), 'Helvetica-Bold'),
    ('FONTSIZE',   (0,0),(-1,-1), 9),
    ('ALIGN',      (0,0),(-1,-1), 'CENTER'),
    ('ROWBACKGROUNDS',(0,1),(-1,-1),[colors.white, TEAL_LIGHT]),
    ('GRID',       (0,0),(-1,-1), 0.5, BORDER_GRAY),
    ('VALIGN',     (0,0),(-1,-1), 'MIDDLE'),
    ('ROWHEIGHT',  (0,0),(-1,-1), 26),
]))
story.append(t)
story.append(SP(4))
story.append(NOTE("After 3-Way Handshake: Both sides agree on sequence numbers. "
                  "Data transfer can begin. Connection is ESTABLISHED."))
story.append(SP(10))

# 5.5 4-Way Handshake
story.append(SEC("5.5  TCP 4-Way Handshake — How a Connection is CLOSED"))
story.append(P(
    "When data transfer is complete, TCP closes the connection gracefully using "
    "a <b>4-Way Handshake</b>. Either side can initiate the closing."
))
story.append(NOTE(
    "Like ending a phone call politely: (1) You: 'I'm done, goodbye' — (2) Friend: "
    "'OK, noted.' — (3) Friend: 'I'm done too, goodbye' — (4) You: 'OK bye!' "
    "Now the call is fully ended."
))
story.append(SP(6))

story.append(StepBox([
    ("FIN",     "Client: 'I am done sending. Closing my side.'"),
    ("ACK",     "Server: 'OK, I received your FIN. But I may still send.'"),
    ("FIN",     "Server: 'Now I'm also done. Closing my side too.'"),
    ("ACK",     "Client: 'Got it! Bye!' Connection fully closed."),
], PURPLE))
story.append(SP(8))

hw4 = [
    ["Step", "Who Sends",     "Message", "Meaning"],
    ["1",    "Client→Server", "FIN",     "I have finished sending data. Please close my side."],
    ["2",    "Server→Client", "ACK",     "OK, I got your FIN. My side may still send data."],
    ["3",    "Server→Client", "FIN",     "Now I am also done. Please close my side too."],
    ["4",    "Client→Server", "ACK",     "Got it. Connection fully closed now."],
]
t2 = Table(hw4, colWidths=[1.5*cm, 3.5*cm, 2.5*cm, 9*cm])
t2.setStyle(TableStyle([
    ('BACKGROUND', (0,0),(-1,0), PURPLE),
    ('TEXTCOLOR',  (0,0),(-1,0), colors.white),
    ('FONTNAME',   (0,0),(-1,0), 'Helvetica-Bold'),
    ('FONTSIZE',   (0,0),(-1,-1), 9),
    ('ALIGN',      (0,0),(-1,-1), 'CENTER'),
    ('ROWBACKGROUNDS',(0,1),(-1,-1),[colors.white, PURPLE_LIGHT]),
    ('GRID',       (0,0),(-1,-1), 0.5, BORDER_GRAY),
    ('VALIGN',     (0,0),(-1,-1), 'MIDDLE'),
    ('ROWHEIGHT',  (0,0),(-1,-1), 26),
]))
story.append(t2)
story.append(SP(4))
story.append(NOTE("Why 4 steps instead of 3? Because the server might still have data "
                  "to send after receiving the client's FIN — so it ACKs first, "
                  "finishes sending, then sends its own FIN."))
story.append(PageBreak())

# 5.6 UDP
story.append(SEC("5.6  UDP — User Datagram Protocol"))
story.append(P(
    "<b>UDP</b> is a <b>connectionless, unreliable</b> protocol. It sends data as "
    "fast as possible without establishing a connection or waiting for acknowledgements. "
    "No guarantees — some packets may be lost, and that's acceptable."
))
story.append(NOTE(
    "UDP is like sending an ordinary postcard. You just write and drop it in the "
    "postbox — no tracking, no confirmation of delivery. It might get lost. "
    "But it's super fast and cheap. Perfect for a quick message!"
))
story.append(SP(6))
for item in [
    "Connectionless: No handshake, no connection setup — just send the data",
    "Unreliable: No acknowledgements, no retransmission of lost packets",
    "No ordering: Packets may arrive out of order — no reordering done",
    "No flow control: Sender sends at full speed regardless of receiver capacity",
    "Very fast: Minimal overhead — small header (only 8 bytes vs TCP's 20 bytes)",
    "Used for: Live video/audio streaming, online gaming, DNS lookups, VoIP (Zoom, WhatsApp calls)",
]:
    story.append(B(item))
story.append(SP(8))

# 5.7 TCP vs UDP
story.append(SEC("5.7  TCP vs UDP — Full Comparison"))
tcp_udp = [
    ["Feature",           "TCP",                         "UDP"],
    ["Full Name",         "Transmission Control Protocol","User Datagram Protocol"],
    ["Connection",        "Connection-oriented (3-way handshake)","Connectionless (no setup)"],
    ["Reliability",       "Reliable (ACK + retransmit)", "Unreliable (no ACK)"],
    ["Ordering",          "Guaranteed order",            "No ordering"],
    ["Speed",             "Slower (overhead)",           "Faster (no overhead)"],
    ["Header Size",       "20 bytes minimum",            "8 bytes (fixed)"],
    ["Flow Control",      "Yes (sliding window)",        "No"],
    ["Congestion Control","Yes",                         "No"],
    ["Error Checking",    "Yes (checksum + ACK)",        "Checksum only"],
    ["Use Case",          "Web, Email, File Transfer, SSH","Video stream, DNS, Gaming, VoIP"],
    ["Example Protocol",  "HTTP, FTP, SMTP, SSH",        "DNS, RTP, DHCP, SNMP"],
    ["Analogy",           "Registered Post (guaranteed)","Postcard (fast, no guarantee)"],
]
t3 = Table(tcp_udp, colWidths=[4.5*cm, 5.5*cm, 6*cm])
style3 = [
    ('BACKGROUND', (0,0),(-1,0), DARK),
    ('TEXTCOLOR',  (0,0),(-1,0), colors.white),
    ('FONTNAME',   (0,0),(-1,0), 'Helvetica-Bold'),
    ('FONTSIZE',   (0,0),(-1,-1), 9),
    ('ALIGN',      (0,0),(-1,-1), 'CENTER'),
    ('VALIGN',     (0,0),(-1,-1), 'MIDDLE'),
    ('FONTNAME',   (0,1),(0,-1), 'Helvetica-Bold'),
    ('GRID',       (0,0),(-1,-1), 0.5, BORDER_GRAY),
    ('ROWHEIGHT',  (0,0),(-1,-1), 22),
]
for i in range(1, len(tcp_udp)):
    style3.append(('BACKGROUND', (1,i),(1,i), TEAL_LIGHT))
    style3.append(('BACKGROUND', (2,i),(2,i), AMBER_LIGHT))
    if i % 2 == 0:
        style3.append(('BACKGROUND', (0,i),(0,i), LIGHT_BG))
t3.setStyle(TableStyle(style3))
story.append(t3)
story.append(PageBreak())

# 5.8 Port Addressing
story.append(SEC("5.8  Port Addressing"))
story.append(P(
    "A <b>port number</b> is a 16-bit number (0–65535) that identifies a specific "
    "application or service on a computer. While an IP address identifies the "
    "computer, the port number identifies the specific application on that computer."
))
story.append(NOTE(
    "An IP address is like the address of a large apartment building. The port "
    "number is the flat number inside. The postman (router) delivers to the "
    "building (IP), but the letter goes to a specific flat (port/application)."
))
story.append(SP(6))

story.append(P("<b>Three ranges of port numbers:</b>"))
port_ranges = [
    ["Range",            "Name",            "Description",                           "Who Uses It"],
    ["0 – 1023",         "Well-Known Ports","Reserved for standard services",        "HTTP=80, HTTPS=443, FTP=21, SSH=22, SMTP=25, DNS=53"],
    ["1024 – 49151",     "Registered Ports","Used by companies for their apps",      "MySQL=3306, PostgreSQL=5432, MongoDB=27017"],
    ["49152 – 65535",    "Dynamic/Private", "Temporary ports assigned by OS",        "Created when you open Chrome, WhatsApp etc."],
]
t4 = Table(port_ranges, colWidths=[3*cm, 3.5*cm, 4.5*cm, 5.5*cm])
t4.setStyle(TableStyle([
    ('BACKGROUND', (0,0),(-1,0), AMBER),
    ('TEXTCOLOR',  (0,0),(-1,0), colors.white),
    ('FONTNAME',   (0,0),(-1,0), 'Helvetica-Bold'),
    ('FONTSIZE',   (0,0),(-1,-1), 8.5),
    ('ALIGN',      (0,0),(-1,-1), 'CENTER'),
    ('VALIGN',     (0,0),(-1,-1), 'MIDDLE'),
    ('ROWBACKGROUNDS',(0,1),(-1,-1),[AMBER_LIGHT, colors.white]),
    ('GRID',       (0,0),(-1,-1), 0.5, BORDER_GRAY),
    ('ROWHEIGHT',  (0,0),(-1,-1), 26),
]))
story.append(t4)
story.append(SP(6))

story.append(SEC("Common Well-Known Ports to Remember"))
ports = [
    ["Port", "Protocol", "Service",  "Analogy"],
    ["20, 21", "FTP",    "File Transfer", "Cargo ship delivering files"],
    ["22",   "SSH",      "Secure Remote Login", "Secure telephone line"],
    ["23",   "Telnet",   "Unsecure Remote Login","Open phone call (not private)"],
    ["25",   "SMTP",     "Sending emails",  "Post office for sending letters"],
    ["53",   "DNS",      "Domain Name lookup","Phone book / directory"],
    ["67/68","DHCP",     "IP address assignment","Hotel receptionist giving room keys"],
    ["80",   "HTTP",     "Web browsing (unsecure)","Open newspaper"],
    ["110",  "POP3",     "Receiving emails (downloads)","Collecting your post from letterbox"],
    ["143",  "IMAP",     "Receiving emails (server-stored)","Reading post at the post office"],
    ["443",  "HTTPS",    "Secure web browsing","Sealed, encrypted letter"],
    ["3306", "MySQL",    "Database",        "Filing cabinet in office"],
]
t5 = Table(ports, colWidths=[2*cm, 2*cm, 5.5*cm, 7*cm])
t5.setStyle(TableStyle([
    ('BACKGROUND', (0,0),(-1,0), BLUE),
    ('TEXTCOLOR',  (0,0),(-1,0), colors.white),
    ('FONTNAME',   (0,0),(-1,0), 'Helvetica-Bold'),
    ('FONTSIZE',   (0,0),(-1,-1), 9),
    ('ALIGN',      (0,0),(1,-1), 'CENTER'),
    ('ALIGN',      (2,0),(-1,-1), 'LEFT'),
    ('ROWBACKGROUNDS',(0,1),(-1,-1),[BLUE_LIGHT, colors.white]),
    ('GRID',       (0,0),(-1,-1), 0.5, BORDER_GRAY),
    ('VALIGN',     (0,0),(-1,-1), 'MIDDLE'),
    ('ROWHEIGHT',  (0,0),(-1,-1), 22),
]))
story.append(t5)
story.append(PageBreak())

# 5.9 Leaky Bucket
story.append(SEC("5.9  Congestion Control — Leaky Bucket Algorithm"))
story.append(P(
    "Congestion happens when too much data floods the network at once, causing "
    "routers to drop packets. <b>The Leaky Bucket algorithm</b> is a traffic shaping "
    "method that controls the rate at which data enters the network — smoothing out "
    "bursts into a steady, predictable flow."
))
story.append(NOTE(
    "Imagine a bucket with a small hole at the bottom. You can pour water in at "
    "ANY rate (bursty traffic) — but the water leaks out at a CONSTANT rate "
    "(controlled output). If you pour too much, the bucket overflows (packets dropped). "
    "The output is always steady, no matter how irregular the input is."
))
story.append(SP(6))

story.append(ColorBox("How Leaky Bucket Works", [
    "Incoming packets (bursty or irregular) are put into a buffer (the 'bucket')",
    "Packets leave the bucket at a FIXED, CONSTANT rate — like water dripping from a hole",
    "If the bucket is full and more packets arrive → they are DROPPED (overflow)",
    "Output is always smooth and predictable, regardless of input pattern",
    "Rate of output = fixed (e.g., always 10 packets per second)",
], TEAL_LIGHT, TEAL))
story.append(SP(6))

lb_data = [
    ["Parameter",        "Leaky Bucket"],
    ["Output rate",      "Fixed and constant always"],
    ["Burst handling",   "Absorbs small bursts up to bucket capacity"],
    ["Overflow",         "Packets dropped if bucket is full"],
    ["Effect",           "Converts bursty traffic into smooth, uniform traffic"],
    ["Use case",         "ATM networks, traffic policing in ISPs"],
    ["Limitation",       "Cannot handle genuine bursty traffic efficiently — bursts always lost"],
]
t6 = Table(lb_data, colWidths=[5*cm, 12*cm])
t6.setStyle(TableStyle([
    ('BACKGROUND', (0,0),(-1,0), TEAL),
    ('TEXTCOLOR',  (0,0),(-1,0), colors.white),
    ('FONTNAME',   (0,0),(-1,0), 'Helvetica-Bold'),
    ('FONTSIZE',   (0,0),(-1,-1), 9.5),
    ('FONTNAME',   (0,1),(0,-1), 'Helvetica-Bold'),
    ('ROWBACKGROUNDS',(0,1),(-1,-1),[TEAL_LIGHT, colors.white]),
    ('GRID',       (0,0),(-1,-1), 0.5, BORDER_GRAY),
    ('VALIGN',     (0,0),(-1,-1), 'MIDDLE'),
    ('ROWHEIGHT',  (0,0),(-1,-1), 24),
    ('LEFTPADDING',(1,1),(1,-1), 8),
]))
story.append(t6)
story.append(SP(10))

# 5.10 Token Bucket
story.append(SEC("5.10  Congestion Control — Token Bucket Algorithm"))
story.append(P(
    "The <b>Token Bucket algorithm</b> is more flexible than Leaky Bucket. "
    "It allows controlled bursts of traffic while still limiting the average rate."
))
story.append(NOTE(
    "Imagine a bucket filling up with tokens (coins) at a steady rate. Each time "
    "you want to send a packet, you must take a token from the bucket. If there are "
    "tokens available, you can send — even multiple packets at once (burst). "
    "If the bucket is empty, you must wait. No tokens = no sending."
))
story.append(SP(6))

story.append(ColorBox("How Token Bucket Works", [
    "Tokens are added to the bucket at a FIXED rate (e.g., 10 tokens/second)",
    "Bucket has a maximum capacity — tokens that exceed the limit are DISCARDED",
    "To send a packet, the sender must TAKE one token from the bucket",
    "If tokens are available → send immediately (bursts are ALLOWED!)",
    "If no tokens → wait until tokens arrive (sender is throttled)",
    "Average rate is controlled, but SHORT BURSTS are permitted up to bucket size",
], PURPLE_LIGHT, PURPLE))
story.append(SP(6))

compare_data = [
    ["Feature",          "Leaky Bucket",                   "Token Bucket"],
    ["Output rate",      "Strictly constant",              "Variable (bursts allowed)"],
    ["Burst handling",   "Bursts are absorbed or dropped", "Bursts are allowed (uses saved tokens)"],
    ["Token concept",    "No tokens — just a drain",       "Tokens accumulate and enable bursts"],
    ["Flexibility",      "Less flexible — rigid output",   "More flexible — burst + avg control"],
    ["When no data",     "Nothing happens",                "Tokens keep accumulating"],
    ["Use case",         "Traffic policing",               "Traffic shaping, internet bandwidth"],
    ["Example",          "ATM (old networks)",             "Modern internet, AWS bandwidth limiting"],
]
t7 = Table(compare_data, colWidths=[4*cm, 5.5*cm, 7*cm])
t7.setStyle(TableStyle([
    ('BACKGROUND', (0,0),(-1,0), DARK),
    ('TEXTCOLOR',  (0,0),(-1,0), colors.white),
    ('FONTNAME',   (0,0),(-1,0), 'Helvetica-Bold'),
    ('FONTSIZE',   (0,0),(-1,-1), 9),
    ('FONTNAME',   (0,1),(0,-1), 'Helvetica-Bold'),
    ('ALIGN',      (0,0),(-1,-1), 'CENTER'),
    ('ROWBACKGROUNDS',(0,1),(-1,-1),[
        (TEAL_LIGHT, PURPLE_LIGHT)[i%2] for i in range(len(compare_data))
    ]),
    ('GRID',       (0,0),(-1,-1), 0.5, BORDER_GRAY),
    ('VALIGN',     (0,0),(-1,-1), 'MIDDLE'),
    ('ROWHEIGHT',  (0,0),(-1,-1), 24),
]))
story.append(t7)
story.append(PageBreak())


# ═══════════════════════════════════════════════════════════
# CHAPTER 6 — APPLICATION LAYER
# ═══════════════════════════════════════════════════════════
story.append(Paragraph("Chapter 6: Application Layer Protocols", ch_title))
story.append(HR())
story.append(SP(4))
story.append(P(
    "The <b>Application Layer</b> is Layer 7 — the topmost layer of the OSI model. "
    "It is the layer that users interact with directly. It provides protocols for "
    "specific applications like web browsing, email, file transfer, and remote login."
))
story.append(NOTE(
    "If the Network Layer is the road system and Transport Layer is the vehicle, "
    "the Application Layer is the actual destination — the shop, hospital, or office "
    "you're trying to reach. It's where the real work happens for the user."
))
story.append(SP(8))

# 6.1 DNS
story.append(SEC("6.1  DNS — Domain Name System"))
story.append(P(
    "<b>DNS</b> translates human-friendly domain names (like www.google.com) into "
    "IP addresses (like 142.250.80.4) that computers can understand. Without DNS, "
    "you'd have to remember IP addresses to visit websites!"
))
story.append(NOTE(
    "DNS is the internet's phone book. You look up a name (google.com), "
    "and it gives you the number (IP address). Just like searching a contact "
    "by name instead of remembering their 10-digit phone number."
))
story.append(SP(6))

story.append(P("<b>How DNS Resolution Works (step by step):</b>"))
dns_steps = [
    ["Step", "What Happens",                              "Who Does It"],
    ["1",    "You type www.google.com in browser",        "You (user)"],
    ["2",    "Browser checks its own cache first",        "Browser / OS"],
    ["3",    "If not cached, asks the Recursive Resolver","Your ISP's DNS server"],
    ["4",    "Resolver asks Root DNS Server ('where is .com?')", "Root DNS (13 in world)"],
    ["5",    "Root says: ask TLD Server for .com",        "Root DNS Server"],
    ["6",    "TLD Server says: ask Google's Name Server", "TLD (.com) Server"],
    ["7",    "Google's Name Server gives the IP address", "Authoritative DNS"],
    ["8",    "Resolver returns IP to your browser",       "Recursive Resolver"],
    ["9",    "Browser connects to 142.250.80.4",          "Your computer"],
]
t8 = Table(dns_steps, colWidths=[1.5*cm, 9.5*cm, 5.5*cm])
t8.setStyle(TableStyle([
    ('BACKGROUND', (0,0),(-1,0), BLUE),
    ('TEXTCOLOR',  (0,0),(-1,0), colors.white),
    ('FONTNAME',   (0,0),(-1,0), 'Helvetica-Bold'),
    ('FONTSIZE',   (0,0),(-1,-1), 9),
    ('ALIGN',      (0,0),(0,-1), 'CENTER'),
    ('ALIGN',      (1,0),(-1,-1), 'LEFT'),
    ('ROWBACKGROUNDS',(0,1),(-1,-1),[BLUE_LIGHT, colors.white]),
    ('GRID',       (0,0),(-1,-1), 0.5, BORDER_GRAY),
    ('VALIGN',     (0,0),(-1,-1), 'MIDDLE'),
    ('ROWHEIGHT',  (0,0),(-1,-1), 22),
    ('LEFTPADDING',(1,1),(1,-1), 6),
]))
story.append(t8)
story.append(SP(4))
story.append(ColorBox("DNS Key Facts", [
    "Uses Port 53  |  Uses both UDP (for queries) and TCP (for zone transfers)",
    "DNS Record Types: A (IPv4 address), AAAA (IPv6), MX (mail server), CNAME (alias), NS (name server)",
    "DNS Caching: Results are cached to speed up future lookups (TTL = Time To Live)",
    "DNS Hierarchy: Root (.root) → TLD (.com, .in, .org) → Domain (google.com) → Subdomain (www.google.com)",
], BLUE_LIGHT, BLUE))
story.append(SP(10))

# 6.2 HTTP/HTTPS
story.append(SEC("6.2  HTTP & HTTPS"))
story.append(P(
    "<b>HTTP (HyperText Transfer Protocol)</b> is the foundation of data communication "
    "on the web. Your browser uses HTTP to request web pages from servers. "
    "<b>HTTPS</b> is the secure version — it encrypts all data using SSL/TLS."
))
story.append(NOTE(
    "HTTP is like sending a postcard — anyone who handles it can read it. "
    "HTTPS is like sending a sealed, locked envelope — only the sender and "
    "receiver can read the contents. Always use HTTPS for sensitive data!"
))
story.append(SP(6))

http_data = [
    ["Feature",     "HTTP",                          "HTTPS"],
    ["Full Name",   "HyperText Transfer Protocol",   "HTTP Secure"],
    ["Port",        "80",                            "443"],
    ["Security",    "No encryption (plain text)",    "Encrypted with SSL/TLS"],
    ["URL starts",  "http://",                       "https://"],
    ["Use case",    "Old/non-sensitive websites",    "Banking, shopping, login pages"],
    ["Analogy",     "Open postcard",                 "Sealed, locked envelope"],
    ["Data safety", "Anyone can read it",            "Only sender & receiver can read"],
]
t9 = Table(http_data, colWidths=[3.5*cm, 6*cm, 7*cm])
st9 = [
    ('BACKGROUND', (0,0),(-1,0), DARK),
    ('TEXTCOLOR',  (0,0),(-1,0), colors.white),
    ('FONTNAME',   (0,0),(-1,0), 'Helvetica-Bold'),
    ('FONTSIZE',   (0,0),(-1,-1), 9),
    ('FONTNAME',   (0,1),(0,-1), 'Helvetica-Bold'),
    ('ALIGN',      (0,0),(-1,-1), 'CENTER'),
    ('GRID',       (0,0),(-1,-1), 0.5, BORDER_GRAY),
    ('VALIGN',     (0,0),(-1,-1), 'MIDDLE'),
    ('ROWHEIGHT',  (0,0),(-1,-1), 22),
]
for i in range(1, len(http_data)):
    st9.append(('BACKGROUND', (1,i),(1,i), RED_LIGHT))
    st9.append(('BACKGROUND', (2,i),(2,i), TEAL_LIGHT))
t9.setStyle(TableStyle(st9))
story.append(t9)
story.append(SP(6))

story.append(P("<b>HTTP Methods (Request Types):</b>"))
for item in [
    "GET — Retrieve data from server (like opening a webpage)",
    "POST — Send data to server (like submitting a login form)",
    "PUT — Update existing data on server",
    "DELETE — Delete data on server",
]:
    story.append(B(item))
story.append(SP(10))

# 6.3 FTP
story.append(SEC("6.3  FTP — File Transfer Protocol"))
story.append(P(
    "<b>FTP</b> is used to transfer files between a client and a server over a "
    "network. It uses TWO connections simultaneously: one for control (commands) "
    "and one for data (actual file transfer)."
))
story.append(NOTE(
    "FTP is like a courier service. You call them (control connection on port 21) "
    "to tell them what to pick up. Then a separate van (data connection on port 20) "
    "comes to actually carry the goods."
))
story.append(SP(6))
story.append(ColorBox("FTP Key Facts", [
    "Uses Port 21 for control (commands like LIST, RETR, STOR)",
    "Uses Port 20 for data transfer (actual file content)",
    "Two modes: Active FTP (server initiates data connection) and Passive FTP (client initiates both)",
    "Plain FTP has NO encryption — passwords sent as plain text!",
    "Secure alternatives: SFTP (SSH File Transfer Protocol) or FTPS (FTP + SSL)",
    "Common uses: Website deployment, uploading files to hosting servers",
], AMBER_LIGHT, AMBER))
story.append(SP(10))

# 6.4 Email protocols
story.append(SEC("6.4  Email Protocols — SMTP, POP3, and IMAP"))
story.append(P(
    "Sending and receiving emails involves THREE different protocols, each with "
    "a specific role."
))
story.append(NOTE(
    "Imagine email like a physical postal system: SMTP is the POST OFFICE "
    "that collects and delivers your letter. POP3 is like picking up your "
    "letters from your letterbox and taking them home (they leave the post office). "
    "IMAP is like reading letters at the post office itself — they stay there, "
    "accessible from anywhere."
))
story.append(SP(6))

email_data = [
    ["Protocol", "Full Name",                    "Port", "Role",                         "Analogy"],
    ["SMTP",     "Simple Mail Transfer Protocol", "25/587","SENDING emails",              "Post office dispatch desk"],
    ["POP3",     "Post Office Protocol v3",       "110",  "RECEIVING (downloads & deletes)","Taking letters home from mailbox"],
    ["IMAP",     "Internet Message Access Protocol","143", "RECEIVING (stays on server)", "Reading mail at post office"],
]
t10 = Table(email_data, colWidths=[2*cm, 5*cm, 2*cm, 4.5*cm, 4*cm])
t10.setStyle(TableStyle([
    ('BACKGROUND', (0,0),(-1,0), RED),
    ('TEXTCOLOR',  (0,0),(-1,0), colors.white),
    ('FONTNAME',   (0,0),(-1,0), 'Helvetica-Bold'),
    ('FONTSIZE',   (0,0),(-1,-1), 9),
    ('ALIGN',      (0,0),(-1,-1), 'CENTER'),
    ('ROWBACKGROUNDS',(0,1),(-1,-1),[RED_LIGHT, colors.white, AMBER_LIGHT]),
    ('GRID',       (0,0),(-1,-1), 0.5, BORDER_GRAY),
    ('VALIGN',     (0,0),(-1,-1), 'MIDDLE'),
    ('ROWHEIGHT',  (0,0),(-1,-1), 30),
    ('FONTNAME',   (0,1),(0,-1), 'Helvetica-Bold'),
]))
story.append(t10)
story.append(SP(6))

story.append(P("<b>POP3 vs IMAP — Key Difference:</b>"))
for item in [
    "POP3: Downloads emails to your device and DELETES from server. Works offline. But if you change device, old emails are gone. Best for one device.",
    "IMAP: Keeps emails on the server. You see the SAME inbox from phone, laptop, tablet. Deleting on one device deletes everywhere. Best for multiple devices (modern approach — Gmail, Outlook use IMAP).",
]:
    story.append(B(item))
story.append(PageBreak())

# 6.5 Telnet & SSH
story.append(SEC("6.5  Remote Login — Telnet and SSH"))
story.append(P(
    "Remote login protocols let you control a computer from another location "
    "over the network — like sitting at that computer's keyboard, but from far away."
))
story.append(NOTE(
    "Remote login is like a remote control for a computer. Telnet is an old "
    "remote control that sends commands over an open (unsecured) channel — "
    "anyone can hear what buttons you press! SSH is a modern remote control "
    "with full encryption — nobody can eavesdrop."
))
story.append(SP(6))

remote_data = [
    ["Feature",    "Telnet",                          "SSH"],
    ["Full Name",  "Teletype Network",                "Secure Shell"],
    ["Port",       "23",                              "22"],
    ["Security",   "NO encryption (plain text)",      "Fully encrypted"],
    ["Password",   "Sent as plain text (dangerous!)", "Encrypted"],
    ["Use Today",  "Rarely — insecure",               "Standard for all remote admin"],
    ["Analogy",    "Walkie-talkie in public",         "Encrypted private phone line"],
    ["Common Use", "Legacy systems only",             "Linux servers, AWS, GitHub"],
]
t11 = Table(remote_data, colWidths=[3.5*cm, 6.5*cm, 6.5*cm])
st11 = [
    ('BACKGROUND', (0,0),(-1,0), DARK),
    ('TEXTCOLOR',  (0,0),(-1,0), colors.white),
    ('FONTNAME',   (0,0),(-1,0), 'Helvetica-Bold'),
    ('FONTSIZE',   (0,0),(-1,-1), 9),
    ('FONTNAME',   (0,1),(0,-1), 'Helvetica-Bold'),
    ('ALIGN',      (0,0),(-1,-1), 'CENTER'),
    ('GRID',       (0,0),(-1,-1), 0.5, BORDER_GRAY),
    ('VALIGN',     (0,0),(-1,-1), 'MIDDLE'),
    ('ROWHEIGHT',  (0,0),(-1,-1), 22),
]
for i in range(1, len(remote_data)):
    st11.append(('BACKGROUND', (1,i),(1,i), RED_LIGHT))
    st11.append(('BACKGROUND', (2,i),(2,i), TEAL_LIGHT))
t11.setStyle(TableStyle(st11))
story.append(t11)
story.append(SP(10))

# 6.6 NFS & SMB
story.append(SEC("6.6  File Sharing — NFS and SMB"))
story.append(P(
    "File sharing protocols allow computers on a network to access and share "
    "files and folders as if they were stored locally on that computer."
))
story.append(NOTE(
    "NFS and SMB are like a shared Google Drive, but for local networks. Instead "
    "of storing a file on one computer and emailing it to others, everyone can "
    "directly access the same folder over the network."
))
story.append(SP(6))

fs_data = [
    ["Feature",  "NFS (Network File System)",        "SMB (Server Message Block)"],
    ["Made By",  "Sun Microsystems (1984)",           "IBM, Microsoft"],
    ["Best For", "Linux/Unix environments",           "Windows environments"],
    ["Port",     "2049",                              "445 (modern), 139 (older)"],
    ["Use",      "Sharing files across Unix/Linux servers","Windows shared folders (\\\\server\\share)"],
    ["Analogy",  "Shared drive in a Linux lab",      "Windows 'My Network Places' / shared folder"],
    ["Modern Use","Cloud storage (NFS v4), Kubernetes","Office Windows file sharing, Samba"],
]
t12 = Table(fs_data, colWidths=[3*cm, 6.5*cm, 7*cm])
st12 = [
    ('BACKGROUND', (0,0),(-1,0), PURPLE),
    ('TEXTCOLOR',  (0,0),(-1,0), colors.white),
    ('FONTNAME',   (0,0),(-1,0), 'Helvetica-Bold'),
    ('FONTSIZE',   (0,0),(-1,-1), 9),
    ('FONTNAME',   (0,1),(0,-1), 'Helvetica-Bold'),
    ('ALIGN',      (0,0),(-1,-1), 'CENTER'),
    ('ROWBACKGROUNDS',(0,1),(-1,-1),[PURPLE_LIGHT, colors.white]),
    ('GRID',       (0,0),(-1,-1), 0.5, BORDER_GRAY),
    ('VALIGN',     (0,0),(-1,-1), 'MIDDLE'),
    ('ROWHEIGHT',  (0,0),(-1,-1), 24),
]
t12.setStyle(TableStyle(st12))
story.append(t12)
story.append(SP(10))

# 6.7 SNMP
story.append(SEC("6.7  SNMP — Simple Network Management Protocol"))
story.append(P(
    "<b>SNMP</b> is used to <b>monitor and manage network devices</b> — routers, "
    "switches, servers, printers — from a central location. It lets network "
    "administrators check device status, collect statistics, and configure devices "
    "remotely."
))
story.append(NOTE(
    "SNMP is like a hospital's nurse monitoring system. The central monitoring "
    "station (SNMP Manager) keeps checking the vital signs (CPU, memory, bandwidth) "
    "of all patients (network devices). If something goes wrong, an alarm "
    "(SNMP Trap) is sent automatically."
))
story.append(SP(6))

story.append(P("<b>Three main SNMP components:</b>"))
for item in [
    "SNMP Manager: The central controller — a software that collects and displays network data (e.g., Nagios, Zabbix)",
    "SNMP Agent: Software running ON each network device (router, switch) — collects local data and responds to manager queries",
    "MIB (Management Information Base): A database/dictionary that defines what data can be monitored (e.g., interface status, packet count, CPU usage)",
]:
    story.append(B(item))
story.append(SP(6))

story.append(ColorBox("SNMP Key Facts", [
    "Uses Port 161 (for queries) and Port 162 (for traps/alerts)",
    "Uses UDP protocol (fast, no connection overhead needed for monitoring)",
    "SNMP Operations: GET (read a value), SET (change a value), TRAP (device alerts manager)",
    "Versions: SNMPv1 (basic), SNMPv2c (improved), SNMPv3 (with authentication & encryption)",
    "Example: Manager asks router: 'How many packets did you drop today?' Agent replies with count",
    "Used by: Network Operations Centers (NOC), cloud providers, enterprise IT teams",
], BLUE_LIGHT, BLUE))
story.append(PageBreak())


# ═══════════════════════════════════════════════════════════
# CHAPTER 7 — EMERGING NETWORKING CONCEPTS
# ═══════════════════════════════════════════════════════════
story.append(Paragraph("Chapter 7: Emerging Networking Concepts", ch_title))
story.append(HR())
story.append(SP(4))
story.append(P(
    "Modern networking is evolving rapidly. Beyond traditional networks, new "
    "paradigms like Cloud Networking, IoT, and SDN are reshaping how we design "
    "and manage networks. These concepts are critical for placement exams and "
    "real-world industry roles."
))
story.append(SP(8))

# 7.1 Cloud Networking
story.append(SEC("7.1  Cloud Networking Basics"))
story.append(P(
    "<b>Cloud Networking</b> refers to networking resources — routers, switches, "
    "firewalls, load balancers — that are hosted and delivered over the internet "
    "by cloud providers (AWS, Azure, Google Cloud) instead of physical hardware "
    "in your own office."
))
story.append(NOTE(
    "Traditional networking is like owning and maintaining your own generator "
    "for electricity. Cloud networking is like using electricity from the city "
    "grid — you don't own the infrastructure, you just pay for what you use, "
    "and it's always available."
))
story.append(SP(6))

for item in [
    "Virtual Networks: Instead of physical cables, you create networks in software (VPCs — Virtual Private Clouds)",
    "Scalability: Need more bandwidth? Just click a button. No physical hardware to buy.",
    "On-Demand: Pay only for what you use (pay-as-you-go model)",
    "Global reach: Your network can span datacenters across the world in minutes",
    "Examples: AWS VPC, Azure Virtual Network, Google Cloud VPN",
]:
    story.append(B(item))
story.append(SP(6))

story.append(ColorBox("Key Cloud Networking Concepts", [
    "VPC (Virtual Private Cloud): Your own isolated private network inside the cloud",
    "CDN (Content Delivery Network): Servers placed near users worldwide for fast content delivery (e.g., Cloudflare, Akamai)",
    "Load Balancer: Distributes incoming traffic across multiple servers to avoid overload",
    "Firewall-as-a-Service: Security rules managed in the cloud, not on physical boxes",
    "SD-WAN: Software-Defined Wide Area Network — manage branch office networks from cloud",
], TEAL_LIGHT, TEAL))
story.append(SP(10))

# 7.2 IoT
story.append(SEC("7.2  Internet of Things (IoT)"))
story.append(P(
    "<b>IoT</b> refers to everyday physical devices — appliances, vehicles, sensors, "
    "machines — that are connected to the internet and can collect, send, and receive "
    "data without human interaction."
))
story.append(NOTE(
    "IoT is like giving a brain and voice to everyday objects. Your refrigerator "
    "orders milk when it runs out. Your AC turns on before you reach home. "
    "A factory machine sends an alert when it needs maintenance. Objects are now "
    "smart, connected, and talk to each other!"
))
story.append(SP(6))

iot_examples = [
    ["Category",      "IoT Examples",                           "What They Do"],
    ["Smart Home",    "Smart bulb, AC, TV, door lock",          "Control via phone app or voice"],
    ["Healthcare",    "Smartwatch, glucose monitor, pacemaker", "Track health, alert doctors"],
    ["Agriculture",   "Soil sensors, drone sprayers",           "Monitor crop health, save water"],
    ["Industry (IIoT)","Factory sensors, conveyor monitors",    "Predictive maintenance, efficiency"],
    ["Smart City",    "Traffic lights, parking sensors",        "Reduce traffic, save energy"],
    ["Transport",     "GPS trackers, self-driving cars",        "Navigation, safety, efficiency"],
]
t13 = Table(iot_examples, colWidths=[3*cm, 5.5*cm, 8*cm])
t13.setStyle(TableStyle([
    ('BACKGROUND', (0,0),(-1,0), AMBER),
    ('TEXTCOLOR',  (0,0),(-1,0), colors.white),
    ('FONTNAME',   (0,0),(-1,0), 'Helvetica-Bold'),
    ('FONTSIZE',   (0,0),(-1,-1), 9),
    ('FONTNAME',   (0,1),(0,-1), 'Helvetica-Bold'),
    ('ROWBACKGROUNDS',(0,1),(-1,-1),[AMBER_LIGHT, colors.white]),
    ('GRID',       (0,0),(-1,-1), 0.5, BORDER_GRAY),
    ('VALIGN',     (0,0),(-1,-1), 'MIDDLE'),
    ('ROWHEIGHT',  (0,0),(-1,-1), 24),
    ('LEFTPADDING',(1,1),(2,-1), 6),
]))
story.append(t13)
story.append(SP(6))
story.append(ColorBox("IoT Challenges", [
    "Security: Millions of small devices with weak security = huge attack surface",
    "Power: Most IoT devices run on batteries — protocols must be very power-efficient",
    "Scale: Billions of devices all communicating — network must handle massive scale",
    "Heterogeneity: Devices from different makers must all talk to each other",
    "Bandwidth: Devices often have very limited bandwidth — need lightweight protocols (MQTT, CoAP)",
], RED_LIGHT, RED))
story.append(PageBreak())

# 7.3 MQTT
story.append(SEC("7.3  MQTT — Message Queuing Telemetry Transport"))
story.append(P(
    "<b>MQTT</b> is a lightweight messaging protocol designed specifically for IoT devices "
    "that have limited processing power, battery, and bandwidth. It uses a "
    "<b>publish-subscribe</b> model rather than the traditional request-response model."
))
story.append(NOTE(
    "MQTT is like a newspaper subscription service. You (subscriber) tell the "
    "newspaper agency (broker): 'Send me the Sports section whenever it's available.' "
    "The journalist (publisher) just writes and submits articles — they don't know "
    "or care who reads them. The agency (broker) manages everything in between."
))
story.append(SP(6))

story.append(P("<b>Publish-Subscribe Model:</b>"))
for item in [
    "Publisher: A device that sends (publishes) data to a topic. Example: Temperature sensor publishes to topic 'home/living-room/temperature'",
    "Broker: A central server that receives all messages and distributes them. Example: Mosquitto broker, AWS IoT Core",
    "Subscriber: A device or app that receives messages from a topic. Example: Your phone app subscribes to 'home/living-room/temperature' and shows the value",
]:
    story.append(B(item))
story.append(SP(6))

story.append(ColorBox("MQTT Key Facts", [
    "Full Name: Message Queuing Telemetry Transport",
    "Port: 1883 (plain) | 8883 (with TLS encryption)",
    "Transport: Runs over TCP/IP",
    "QoS Levels: 0 (at most once), 1 (at least once), 2 (exactly once)",
    "Very lightweight: Tiny header (2 bytes minimum) — perfect for constrained devices",
    "Used by: Facebook Messenger (originally!), smart home systems, industrial IoT, AWS IoT",
], PURPLE_LIGHT, PURPLE))
story.append(SP(10))

# 7.4 CoAP
story.append(SEC("7.4  CoAP — Constrained Application Protocol"))
story.append(P(
    "<b>CoAP</b> is another IoT protocol, but it follows the same <b>request-response</b> "
    "model as HTTP — making it easy for web developers to use. However, it is much "
    "lighter than HTTP and works over UDP instead of TCP."
))
story.append(NOTE(
    "CoAP is like a simplified, lightweight version of HTTP designed for tiny "
    "devices. If HTTP is a full-sized bus for carrying web traffic, CoAP is a "
    "bicycle — same roads (internet), much smaller and faster for short trips."
))
story.append(SP(6))

coap_data = [
    ["Feature",     "CoAP",                         "MQTT",                          "HTTP"],
    ["Model",       "Request-Response (like HTTP)",  "Publish-Subscribe",             "Request-Response"],
    ["Transport",   "UDP (fast, lightweight)",        "TCP (reliable)",                "TCP"],
    ["Overhead",    "Very low",                       "Very low",                      "High"],
    ["Best for",    "Direct device-to-device comm",  "Many devices to one broker",    "Web browsers"],
    ["Reliability", "Optional (CON messages)",        "QoS levels 0,1,2",             "TCP guarantees"],
    ["Port",        "5683",                           "1883",                          "80/443"],
    ["Use case",    "Smart meters, sensors",          "Smart home, industrial IoT",    "Web apps"],
]
t14 = Table(coap_data, colWidths=[3*cm, 4.5*cm, 4.5*cm, 4.5*cm])
t14.setStyle(TableStyle([
    ('BACKGROUND', (0,0),(-1,0), DARK),
    ('TEXTCOLOR',  (0,0),(-1,0), colors.white),
    ('FONTNAME',   (0,0),(-1,0), 'Helvetica-Bold'),
    ('FONTSIZE',   (0,0),(-1,-1), 8.5),
    ('FONTNAME',   (0,1),(0,-1), 'Helvetica-Bold'),
    ('ALIGN',      (0,0),(-1,-1), 'CENTER'),
    ('ROWBACKGROUNDS',(0,1),(-1,-1),[
        colors.HexColor("#EAF3FD"), colors.white
    ]),
    ('GRID',       (0,0),(-1,-1), 0.5, BORDER_GRAY),
    ('VALIGN',     (0,0),(-1,-1), 'MIDDLE'),
    ('ROWHEIGHT',  (0,0),(-1,-1), 24),
]))
story.append(t14)
story.append(SP(10))

# 7.5 SDN
story.append(SEC("7.5  Software-Defined Networking (SDN)"))
story.append(P(
    "<b>SDN</b> is a revolutionary approach to networking where the <b>control plane</b> "
    "(the brain that decides where traffic goes) is separated from the <b>data plane</b> "
    "(the hardware that actually forwards traffic). The entire network is controlled "
    "by software from a central controller."
))
story.append(NOTE(
    "Traditional networking is like having a separate driver in every vehicle — "
    "each car (router/switch) makes its own decisions. SDN is like having one "
    "central traffic control tower that tells every vehicle exactly where to go "
    "at every moment. The vehicles just follow instructions — they don't think."
))
story.append(SP(6))

story.append(P("<b>Traditional Network vs SDN:</b>"))
for item in [
    "Traditional: Each router/switch has its own control logic (brain inside the box). Hard to change, expensive hardware, slow to reconfigure.",
    "SDN: A central SOFTWARE controller manages all network devices. Devices become simple forwarding machines. Control is programmable and flexible.",
]:
    story.append(B(item))
story.append(SP(6))

story.append(P("<b>Three Layers of SDN Architecture:</b>"))
sdn_layers = [
    ["Layer",           "What It Contains",                     "Example"],
    ["Application Layer","Business logic, network apps",        "Load balancer app, firewall app, monitoring tool"],
    ["Control Layer",   "SDN Controller (the BRAIN)",           "OpenDaylight, ONOS, Cisco ACI, VMware NSX"],
    ["Data/Infrastructure Layer","Physical network devices",   "Switches, routers — just forward packets as told"],
]
t15 = Table(sdn_layers, colWidths=[4*cm, 6.5*cm, 6*cm])
t15.setStyle(TableStyle([
    ('BACKGROUND', (0,0),(-1,0), PURPLE),
    ('TEXTCOLOR',  (0,0),(-1,0), colors.white),
    ('FONTNAME',   (0,0),(-1,0), 'Helvetica-Bold'),
    ('FONTSIZE',   (0,0),(-1,-1), 9),
    ('FONTNAME',   (0,1),(0,-1), 'Helvetica-Bold'),
    ('ALIGN',      (0,0),(-1,-1), 'CENTER'),
    ('ROWBACKGROUNDS',(0,1),(-1,-1),[PURPLE_LIGHT, AMBER_LIGHT, TEAL_LIGHT]),
    ('GRID',       (0,0),(-1,-1), 0.5, BORDER_GRAY),
    ('VALIGN',     (0,0),(-1,-1), 'MIDDLE'),
    ('ROWHEIGHT',  (0,0),(-1,-1), 30),
    ('LEFTPADDING',(1,1),(-1,-1), 6),
]))
story.append(t15)
story.append(SP(6))

story.append(ColorBox("SDN Key Benefits", [
    "Centralized control: One controller manages entire network — simpler management",
    "Programmability: Network behavior can be changed with software, not hardware replacement",
    "Cost reduction: Use cheap commodity hardware instead of expensive proprietary equipment",
    "Agility: Respond to network changes in seconds (software update) instead of weeks (hardware)",
    "Used by: Google (B4 WAN), Facebook, Microsoft Azure, AWS, all major cloud providers",
    "Key protocol: OpenFlow — standardized communication between controller and switches",
], PURPLE_LIGHT, PURPLE))
story.append(PageBreak())


# ═══════════════════════════════════════════════════════════
# QUICK REVISION SUMMARY
# ═══════════════════════════════════════════════════════════
story.append(Paragraph("Quick Revision Summary — All Three Chapters", ch_title))
story.append(HR())
story.append(SP(4))
story.append(NOTE("Read this page 15 minutes before your exam. All key facts in one place!"))
story.append(SP(6))

story.append(ColorBox("Chapter 5: Transport Layer — Key Points", [
    "Transport Layer = Layer 4 = Process-to-process delivery using PORT NUMBERS",
    "TCP = Reliable, ordered, connection-oriented. Uses 3-way handshake (SYN, SYN-ACK, ACK)",
    "TCP close = 4-way handshake (FIN, ACK, FIN, ACK)",
    "UDP = Fast, unreliable, connectionless. No handshake. Used in video, gaming, DNS",
    "Port ranges: 0-1023=Well-known | 1024-49151=Registered | 49152-65535=Dynamic",
    "Key ports: HTTP=80, HTTPS=443, FTP=21, SSH=22, DNS=53, SMTP=25, POP3=110, IMAP=143",
    "Leaky Bucket: Fixed output rate, bursts dropped if bucket full — rigid traffic shaping",
    "Token Bucket: Tokens accumulate, bursts ALLOWED up to bucket size — flexible",
], TEAL_LIGHT, TEAL))
story.append(SP(6))

story.append(ColorBox("Chapter 6: Application Layer — Key Points", [
    "DNS: Translates domain names to IP. Port 53. Root→TLD→Authoritative name server",
    "HTTP: Web protocol, Port 80, plain text. HTTPS: Port 443, encrypted with SSL/TLS",
    "FTP: File transfer. Port 21 (control) + Port 20 (data). Insecure — use SFTP instead",
    "SMTP (Port 25/587): SENDING emails | POP3 (Port 110): Receive & DOWNLOAD | IMAP (Port 143): Receive, stays on server",
    "Telnet (Port 23): Insecure remote login — avoid! SSH (Port 22): Secure encrypted remote login",
    "NFS: File sharing for Linux/Unix networks | SMB: File sharing for Windows networks",
    "SNMP (Port 161/162): Monitor/manage network devices. Manager + Agent + MIB",
], PURPLE_LIGHT, PURPLE))
story.append(SP(6))

story.append(ColorBox("Chapter 7: Emerging Concepts — Key Points", [
    "Cloud Networking: Network resources (routers, firewalls) hosted in cloud. VPC, CDN, Load Balancer",
    "IoT: Everyday devices (fridges, sensors, cars) connected to internet. Challenges: security, power, scale",
    "MQTT: Publish-Subscribe protocol for IoT. Broker-based. Port 1883. Runs on TCP. Very lightweight",
    "CoAP: HTTP-like protocol for IoT. Runs on UDP. Port 5683. Request-Response model. Very lightweight",
    "SDN: Separates control plane (brain) from data plane (forwarding). Central software controller",
    "SDN layers: Application → Control (controller) → Data/Infrastructure (switches/routers)",
    "SDN protocol: OpenFlow. Used by: Google, AWS, Azure, Facebook in their data centers",
], AMBER_LIGHT, AMBER))
story.append(SP(8))

story.append(SEC("Memory Tricks for Exam"))
tricks = [
    ["Topic",              "Easy Memory Trick"],
    ["3-Way Handshake",    "SYN → SYN-ACK → ACK  =  'Hello?' → 'Hello! Can you hear me?' → 'Yes!'"],
    ["4-Way Handshake",    "FIN, ACK, FIN, ACK  =  'I'm done' → 'OK' → 'Me too' → 'OK bye!'"],
    ["TCP vs UDP",         "TCP = Registered post (slow, guaranteed). UDP = Postcard (fast, might lose)"],
    ["Leaky vs Token Bucket","Leaky = Always drips same rate (rigid). Token = Save tokens, burst later (flexible)"],
    ["SMTP/POP3/IMAP",     "SMTP = Sends. POP3 = Pulls & Purges. IMAP = Inbox stays on server"],
    ["Telnet vs SSH",      "Telnet = Open walkie-talkie. SSH = Encrypted private call"],
    ["MQTT vs CoAP",       "MQTT = Pub-Sub (via broker). CoAP = Request-Response (like HTTP but tiny)"],
    ["SDN",                "Traditional = Each router is its own boss. SDN = One boss controls all routers"],
]
t16 = Table(tricks, colWidths=[4*cm, 13*cm])
t16.setStyle(TableStyle([
    ('BACKGROUND', (0,0),(-1,0), DARK),
    ('TEXTCOLOR',  (0,0),(-1,0), colors.white),
    ('FONTNAME',   (0,0),(-1,0), 'Helvetica-Bold'),
    ('FONTSIZE',   (0,0),(-1,-1), 9),
    ('FONTNAME',   (0,1),(0,-1), 'Helvetica-Bold'),
    ('TEXTCOLOR',  (0,1),(0,-1), TEAL),
    ('ALIGN',      (0,0),(0,-1), 'CENTER'),
    ('ALIGN',      (1,0),(1,-1), 'LEFT'),
    ('ROWBACKGROUNDS',(0,1),(-1,-1),[LIGHT_BG, colors.white]),
    ('GRID',       (0,0),(-1,-1), 0.5, BORDER_GRAY),
    ('VALIGN',     (0,0),(-1,-1), 'MIDDLE'),
    ('ROWHEIGHT',  (0,0),(-1,-1), 26),
    ('LEFTPADDING',(1,1),(1,-1), 8),
]))
story.append(t16)

# ── Build ──────────────────────────────────────────────────────────────
doc.build(story)
print("PDF created successfully!")