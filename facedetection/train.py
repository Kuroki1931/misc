import torch
import torch.optim as optim
import torch.nn as nn
import tqdm
from net import Net
import load_data
import config as cfg
from torchsummary import summary

n_epochs = 20
net = Net()
summary(net, (1, 36, 36))

criterion = nn.CrossEntropyLoss()
optimizer = optim.Adam(net.parameters())

train_folder = cfg.train_images
test_folder = cfg.test_images

train_loader, valid_loader, test_loader = load_data.load(train_folder, test_folder)

class EarlyStoppingCallback:
    """Return True or False on call if the loss increased or not during the last {patience} epochs."""
    def __init__(self, patience = 2):
        self.previous_losses = [float("inf")]
        self.patience = patience
    def __call__(self, val_loss, net):
        if self.evaluate(val_loss, net):
            self.previous_losses.append(val_loss)
            return True
        return False
    def evaluate(self, val_loss, net):
        min_loss = min(self.previous_losses)
        if val_loss < min_loss:
            torch.save(net.state_dict(), 'checkpoint.pt')
        else:
            best_loss_index = self.previous_losses.index(min_loss)
            if best_loss_index <= len(self.previous_losses) - self.patience:
                return False
        return True

es_callback = EarlyStoppingCallback(patience=2)

print('Starting training.\n')

for epoch in range(1, n_epochs+1):
    running_loss = 0.0
    i = 1
    progress_bar = tqdm.tqdm(train_loader)
    for data, target in progress_bar:
        # zero the parameter gradients
        optimizer.zero_grad()

        # forward + backward + optimize
        outputs = net(data)
        loss = criterion(outputs, target)
        loss.backward()
        optimizer.step()

        # print statistics
        running_loss += loss.item()
        progress_bar.set_description(f"{running_loss/i:.4f} ")
        i += 1
    val_loss = 0.0
    for data, target in tqdm.tqdm(valid_loader):
        outputs = net(data)
        loss = criterion(outputs, target)
        val_loss += loss.item()
    val_loss /= len(valid_loader)
    print(f'val loss : {val_loss}')
    if not es_callback(val_loss, net):
        net.load_state_dict(torch.load('checkpoint.pt'))
        break

correct = 0
total = 0
with torch.no_grad():
    for data in tqdm.tqdm(test_loader):
        images, labels = data
        outputs = net(images)
        _, predicted = torch.max(outputs.data, 1)
        total += labels.size(0)
        correct += (predicted == labels).sum().item()

print(f'Accuracy of the network on the {len(test_loader)} test images: {100 * correct / total:.2f} %')
