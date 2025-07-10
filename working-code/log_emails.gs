function getSubjects() {
  const threads = GmailApp.search('is:unread');

  if (threads.length === 0) {
    Logger.log('No unread emails found.');
    return;
  }

  Logger.log(`Found ${threads.length} unread email threads.`);
  return threads;
}

function getStarred(thread) {
  if (thread.hasStarredMessages()) {
    return "Yes";
  } else {
    return "No";
  }
}

function getTags(thread) {
  const labels = thread.getLabels();
  const tags = labels.map(label => label.getName()).join(", ");
  return tags;
}

function getAttatchmentSize(thread) {
  var totalSize = 0;
  const messages = thread.getMessages();

  for (const message of messages) {
    const attachments = message.getAttachments();
    for (const attachment of attachments) {
      totalSize += attachment.getSize()
    }
  }
  var sizeMB = (totalSize / (1024 * 1024))
  return Math.round(sizeMB * 1000) / 1000;
}

function addToSheet(info, sheetId) {
  Logger.log("Adding subject line");
  const sheet = SpreadsheetApp.openById(sheetId);

  sheet.appendRow(info);
}

function writeAllInfo() {
  const threads = getSubjects();
  const sheetId = "17X3hpLVQ1LUWV6hzy9eyN-svP5Wak1ReLMbIlC2oDOA";
  for (const thread of threads) {
    const fullDate = thread.getMessages()[0].getDate();
    const date = Utilities.formatDate(fullDate, Session.getScriptTimeZone(), "dd-MM-yyyy");
    const sender = thread.getMessages()[0].getFrom();
    const subject = thread.getMessages()[0].getSubject();
    const isStarred = getStarred(thread);
    const tags = getTags(thread);
    const size = getAttatchmentSize(thread);

    info = [date, sender, subject, isStarred, tags, size];

    addToSheet(info, sheetId);
  }
}

