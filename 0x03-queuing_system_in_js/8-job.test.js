import { expect } from 'chai';
import kue from 'kue';
import createPushNotificationsJobs from './8-job';

describe('createPushNotificationsJobs', () => {
  let queue;

  before(() => {
    queue = kue.createQueue();
    queue.testMode.enter();
  });

  after(() => {
    queue.testMode.clear();
    queue.testMode.exit();
  });

  it('should create jobs in the queue', () => {
    const jobs = [
      { phoneNumber: '1234567890', message: 'Hello, World!' },
      { phoneNumber: '0987654321', message: 'Goodbye, World!' },
    ];

    createPushNotificationsJobs(jobs, queue);

    const jobCount = queue.testMode.jobs.length;
    expect(jobCount).to.equal(2);

    for (const job of queue.testMode.jobs) {
      expect(job.type).to.equal('push_notification_code_3');
      expect(job.data).to.have.property('phoneNumber');
      expect(job.data).to.have.property('message');
    }
  });
});

