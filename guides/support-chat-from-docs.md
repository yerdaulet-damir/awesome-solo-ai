# Answer Users' Questions from Your Docs with a Support Chat

For a solo founder whose product already has users asking questions. You give a hosted support chat a few docs, check it answers what they cover and admits what they don't, then turn the missed question into a docs update and a reply. This run used [Deacon](https://heydeacon.com) on 25 and 26 October 2026, and every reply below is quoted as it came. To build the chat yourself instead, see the [RAG chatbot playbook](../playbooks/rag-chatbot-over-docs.md).

## Setup

- A Deacon account. Sign up at heydeacon.com with an email address or Google.
- The free plan, which needs no card and has no end date. It gives 50 answers a month, 1 MB of knowledge (about 67 pages of docs), 10 web pages fetched a month and 1 seat. Pasted text doesn't use the 10 pages, and test chats in the Playground don't use answers.
- A few docs. I used three short sample docs, about 250 words each, for a made-up invoicing app called Tallybird. They're at the end.
- An email address you own, to test a reply.

## Steps

1. **Add a doc.** Setup asks for your website. Choose "No website? Add a document or some text", name your product and paste a doc. It trained in under 20 seconds. On the install step, choose "I'll do this later".
2. **Add the rest.** In Knowledge Sources, choose Add text for each doc.
3. **Ask a question the docs cover** in the Playground, which shows the real widget.
4. **Ask ones they don't.** No doc mentions currencies or an iPhone app, so I asked about both. Deacon declined each and asked "Want the team to follow up?" with an email box. I left my address on the euros one.
5. **Find it as the founder.** In Conversations the missed question reads "No answer in your content", with Answer this and Dismiss.
6. **Reply to the person** from the box under the conversation. Deacon steps back on that chat until you choose Hand back to Deacon.
7. **Fix the docs.** Press Answer this, write the answer and Save. Deacon adds it to its help document and shows what it now says.
8. **Ask again** in a new Playground chat.

## Check the result

A question the docs cover:

> **Q:** Can I get a refund on an annual plan?
>
> **Deacon:** Yes, if you cancel within 14 days of the payment, an annual plan is refunded in full. You can cancel under Settings, then Billing, then Cancel plan. After 14 days, annual plans are not refunded, and you keep access until the end of the year you paid for.

Conversations named the refunds doc as its source.

A question they don't:

> **Q:** Is there a Tallybird app for iPhone?
>
> **Deacon:** I don't have the answer to that. Leave your email below and the team will get back to you about whether there is a Tallybird app for iPhone.

The fix I wrote in Answer this, for the euros question:

> Yes. Each client has its own currency. Open the client, choose Edit, and pick a currency under Currency, such as Euro, Pound or US dollar. Every invoice to that client is then in that currency.

The same question in a new chat:

> **Deacon:** Yes. Open the client, choose Edit, and pick Euro under Currency. Every invoice sent to that client will then be in euros.

My reply from Conversations reached the address I'd left about a minute later, by email, with the whole conversation. Emails from Playground chats start "[Test]".

## Sources and test notes

- Tested 25 October 2026 on heydeacon.com, on the free plan, in Chrome, and the chats re-run on 26 October 2026 in a fresh team with the same three docs. The replies above are from 26 October. An AI agent, Claude in Chrome, drove the browser on a test account.
- Answers used: 0 of 50, read from the plan page before and after.
- Not tested: Deacon installed on a real site, What needs you with real visitors, the reply as the visitor sees it in the widget, and what happens at 50 answers.
- Tallybird and its docs were made up for this test.
- Sources: [pricing](https://heydeacon.com/pricing) and [features](https://heydeacon.com/features). Deacon is a hosted, closed-source service.
- I'm one of Deacon's founders.

<details>
<summary>The three sample docs, pasted as text</summary>

**Getting started with Tallybird**

```text
Getting started with Tallybird

Tallybird is an invoicing app for freelancers. You add your clients, send invoices by email, and see who has paid.

Create your account
Sign up at tallybird.example with your email address or a Google account. You don't need a card to start. Your first 14 days are on the Studio plan for free.

Add your first client
Open Clients and choose New client. Enter the client's name and the email address that should receive invoices. You can also add a company name, a postal address and a tax number if you need them on the invoice.

Send your first invoice
Open Invoices and choose New invoice. Pick the client, add one line for each piece of work with a description, a quantity and a price, and set the due date. The default due date is 14 days after the invoice date. Choose Preview to check the invoice, then Send. The client gets an email with a link to view the invoice and download it as a PDF.

Get paid
Connect Stripe under Settings, then Payments, and every invoice gets a Pay now button so the client can pay by card. If you don't connect Stripe, the invoice shows your bank details instead, and you mark it as paid yourself when the money arrives.

Reminders
Tallybird emails your client a polite reminder 3 days before the due date and again 7 days after it. You can turn reminders off for any client from that client's page.
```

**Plans and billing**

```text
Tallybird plans and billing

Tallybird has two plans.

Solo costs $9 a month or $90 a year. It includes up to 10 active clients, unlimited invoices, card payments through Stripe and automatic reminders.

Studio costs $24 a month or $240 a year. It includes unlimited clients, up to 3 team members, recurring invoices, expense tracking, and your own logo and colours on invoices.

Both plans include every update, email support, and PDF downloads of every invoice you have sent.

The free trial
New accounts get 14 days of Studio for free, with no card needed. When the trial ends you move to Solo automatically if you have 10 clients or fewer. If you have more than 10, Tallybird asks you to choose a plan before you can send another invoice. Nothing is deleted.

Paying
We take Visa, Mastercard and American Express. Annual plans can also be paid by bank transfer: email billing@tallybird.example and we will send you an invoice. Your card is charged on the same day each month or year as your first payment.

Changing plan
You can move from Solo to Studio at any time under Settings, then Billing. You pay the difference for the rest of the current period, and the new limits apply straight away. Moving from Studio to Solo takes effect at the end of the period you have already paid for.

Receipts
We email a receipt after every payment. You can also download all of your receipts under Settings, then Billing, then Receipts.
```

**Cancelling and refunds**

```text
Cancelling Tallybird and getting a refund

You can cancel at any time from Settings, then Billing, then Cancel plan. You don't need to email us.

What happens when you cancel
Your plan stays active until the end of the period you have already paid for. After that, your account becomes read-only. You can still log in, view and download every invoice and receipt, and export your client list as a CSV file, but you can't send new invoices. We keep your data for 12 months after your plan ends, then delete it. We email you 30 days before we delete anything.

Refunds
Monthly plans are not refunded, but you keep access until the end of the month you paid for.

Annual plans are refunded in full if you cancel within 14 days of the payment. After 14 days, annual plans are not refunded, and you keep access until the end of the year you paid for.

If we charged you by mistake, for example twice in one month, we always refund the extra payment. Email billing@tallybird.example with the date of the charge.

Refunds go back to the card you paid with and take 5 to 10 working days to arrive.

Coming back
You can restart a plan at any time within those 12 months, and everything will be where you left it.

Deleting your account
To delete your account and all of your data straight away, go to Settings, then Account, then Delete account. This can't be undone.
```

</details>
