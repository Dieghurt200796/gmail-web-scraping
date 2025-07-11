function getEmails() {
  const threads = GmailApp.search('is:unread newer_than:1h');

  if (threads.length === 0) {
    Logger.log('No unread emails found.');
    return;
  }

  Logger.log(`Found ${threads.length} unread email threads.`);
  return threads;
}



function filterSubjects(thread) {
  var subject = thread.getMessages()[0].getSubject();
  if (subject.match(/^to read$/i)) {
    GmailApp.markThreadRead(thread);
    GmailApp.moveThreadToTrash(thread);
    return true
  }
  return false
}

function getLink(message) {
  const match = message.match(/https?:\/\/[^\s"]+/);
  if (match) {
    return match[0];
  }
  Logger.log("No link found.")
  return false
}

function addToDoc(link, docId) {
  Logger.log("Adding link");
  const doc = DocumentApp.openById(docId);

  const body = doc.getBody();

  body.appendParagraph(link);
}

function main() {
  const docId = "1udGYXrJF0ROvKisLl7kFXQ_Q2Ivd0fs8b_mMFE_zsPg";
  const threads = getEmails();
  for (const thread of threads) {
    if (filterSubjects(thread)) {
      var link = getLink(thread.getMessages()[0].getBody());
      if (link) {
        addToDoc(link, docId);
      }
    }
  }
}