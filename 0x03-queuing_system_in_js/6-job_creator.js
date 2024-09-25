import { createQueue } from 'kue';

const queue = createQueue({name: 'push_notification_code'});

const jobData = queue.create('push_notification_code', {
	phoneNumber: '0021234485766',
	message: 'This is the code to verify your account',
});

jobData.on('enqueue', () => {
	console.log('Notification job created: '.concat(jobData.id));
});

jobData.on('complete', () => {
	console.log('Notification job completed');
});

jobData.on('failed attempt', () => {
	console.log('Notification job failed');
});

jobData.save();
