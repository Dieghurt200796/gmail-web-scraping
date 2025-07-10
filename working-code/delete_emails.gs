function getEmails() {
  const threads = GmailApp.search('is:unread older_than:1y', 0, 500);

  if (threads.length === 0) {
    Logger.log('No unread emails older than one year found.');
    return;
  }

  Logger.log(`Found ${threads.length} unread email thread(s).`);
  return threads;
}

function deleteEmails(threads) {
  for (let i = 0; i < threads.length; i += 100) {
    const batch = threads. slice(i, i + 100);

    GmailApp.markThreadsRead(batch);
    GmailApp.moveThreadsToTrash(batch);
  }
}

function main() {
  threads = getEmails();
  if (threads){
    deleteEmails(threads);
  }
}