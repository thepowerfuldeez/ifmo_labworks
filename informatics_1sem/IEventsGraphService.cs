using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;

namespace EventsGraphNavigator.Interaction
{
    #region common

    public interface ITreeViewer<TNode> : IRemoteObject
        where TNode : NamedEntityBaseType
    {
        TNode GetEntity(Guid entityId);
        IEventManager<ITreeEventListener<TNode>> UpdateEvents { get; }

        void ForceChilds(Guid entityId);
    }

    public interface ITreeManager<TNode> : IRemoteObject, ITreeViewer<TNode>
        where TNode : NamedEntityBaseType
    {
        Guid CreateEntity(Guid parentId, String name);
        void SetEntityInfo(TNode entity);

        void MoveItem(Guid entityId, Guid newParentId);
        void DeleteItem(Guid entityId);
    }

    public interface ITreeEventListener<TNode> : IRemoteObject
    {
        void OnNewEntity(Guid parentId, Guid newEntityId);
        void OnUpdateEntity(Guid entityId);
        void OnRemoveEntity(Guid entityId);
        void OnChangeDetected(Guid entityId, object args);
    }

    public interface IEventManager<T> : IRemoteObject
        where T : IRemoteObject
    {
        void AddListener(T listenerInstance);
        void RemoveListener(T listenerInstance);
    }

    #endregion

    public interface IEventsGraphService : IRemoteObject
    {
        IManagementSession OpenManagementSession(string login, string password);
    }

    public interface IManagementSession : IRemoteObject, IDisposable
    {
        IProfileController Profile { get; }

        ISourcesManager Sources { get; }

        IGraphController Graph { get; }

        ITasksQueueService Activities { get; }
    }

    public interface IProfileController : IRemoteObject
    {
        IPatternsManager Patterns { get; }

        // profile export&import
    }

    public interface IPatternsManager : IRemoteObject
    {
        ITreeManager<PatternsFolderEntityType> Folders { get; }
        ITreeManager<PatternsRegexPatternEntityType> Regexes { get; }
        ITreeManager<PatternsTagPatternEntityType> Tags { get; }
        ITreeManager<PatternsLinePatternEntityType> Lines { get; }

        TagPatternInfoType GetTagPatternInfo(Guid tagPatternId);
        void SetTagPatternInfo(TagPatternInfoType info);

        LinePatternInfoType GetLinePatternInfo(Guid linePatternId);
        void SetLinePatternInfo(LinePatternInfoType info);
    }

    public interface ISourcesManager : IRemoteObject
    {
        ITreeManager<SourcesFolderEntityType> Folders { get; }
        ITreeManager<SourcesSourceEntityType> Sources { get; }

        SourceInfoType GetSourceInfo(Guid sourceId);
        void SetSourceInfo(SourceInfoType info);

        void EnableLiveNotifications(Guid sourceId);
        void DisableLiveNotifications(Guid sourceId);

        void RescanSource(Guid sourceId);
        bool IsRunning();
        void Start();
        void Stop();
        // void RefreshSourcesStatus();
    }

    public interface IGraphController : IRemoteObject
    {
        LogMessageEntityType GetMessage(Guid messageId);
        IMessagesQueryResultViewController QueryMessages(LogMessagesQueryInfoType query);
        IMessagesQueryNotificationWatcherController CreateMessagesWatcher(LogMessagesQueryInfoType query);

        TagInstanceEntityType GetTagInstance(Guid tagInstanceId);
        ITagInstacesQueryResultViewController QueryTagInstances(TagInstancesQueryInfoType query);
        ITagInstacesQueryNotificationWatcherController CreateTagsWatcher(LogMessagesQueryInfoType query);
    }

    public interface IMessagesQueryResultViewController : IQueryResultViewController<LogMessagesQueryInfoType, LogMessageEntityType, LogMessagesEntityType>
    {
    }

    public interface ITagInstacesQueryResultViewController : IQueryResultViewController<TagInstancesQueryInfoType, TagInstanceEntityType, TagInstancesEntityType>
    {
    }

    public interface IQueryResultViewController<TQuery, TItem, TItemsCollection> : IRemoteObject, IDisposable
        where TQuery : QueryInfoType
        where TItem : IdentifiedEntityBaseType
        where TItemsCollection : IQueryResultItemsCollection<TItem>
    {
        TQuery QueryInfo { get; }

        int ResultsCount { get; }
        TItemsCollection GetRange(int from, int to);
    }

    public interface IQueryResultItemsCollection<TItem>
    {
        List<TItem> Items { get; }
    }

    public interface IMessagesQueryNotificationWatcherController : IQueryNotificationWatcherController<LogMessagesQueryInfoType, LogMessageEntityType, LogMessagesEntityType>
    {
    }

    public interface ITagInstacesQueryNotificationWatcherController : IQueryNotificationWatcherController<TagInstancesQueryInfoType, TagInstanceEntityType, TagInstancesEntityType>
    {
    }

    public interface IQueryNotificationWatcherController<TQuery, TItem, TItemsCollection> : IRemoteObject, IDisposable
        where TQuery : QueryInfoType
        where TItem : IdentifiedEntityBaseType
        where TItemsCollection : IQueryResultItemsCollection<TItem>
    {
        TQuery QueryInfo { get; }

        IEventManager<IQueryNotificationListener<GuidsList>> ThinItemsAppearedEvent { get; }
        IEventManager<IQueryNotificationListener<GuidsList>> ThinItemsGoneEvent { get; }
        IEventManager<IQueryNotificationListener<TItemsCollection>> ThickItemsAppearedEvent { get; }
        IEventManager<IQueryNotificationListener<TItemsCollection>> ThickItemsGoneEvent { get; }
    }

    public interface IQueryNotificationListener<TArg> : IRemoteObject
    {
        void OnNotification(TArg arg);
    }

    public interface ITasksQueueService
    {
        ITreeViewer<TaskEntityType> Tasks { get; }
    }
}
