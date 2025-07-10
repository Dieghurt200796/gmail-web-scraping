function getSubjects() {
  const threads = GmailApp.search('is:unread in:inbox');

  if (threads.length === 0) {
    Logger.log('No unread emails found.');
    return;
  }

  Logger.log(`Found ${threads.length} unread email threads.`);
  Logger.log('--- Unread Email Subjects ---');

  for (const thread of threads) {
    const firstMessage = thread.getMessages()[0];
    const subject = firstMessage.getSubject();

    Logger.log(subject);
  }
}
